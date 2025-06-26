from pathlib import Path
import re


header_file = '/home/mouzounb/Bureau/cascade_ECS_stock_aval/Code_C/cascade_ECS__stock_aval_ert_rtw/cascade_ECS_stock_aval.h'
model_name = Path(header_file).stem


with open(header_file, 'r') as f:
    content = f.readlines()

# one string
content = ''.join(content)

# select only inputs and outputs
# todo: support states management
content = content.split(u'\n/*')
content = [f'\n/*{e}' 
           for e in content 
           if e.startswith(" External inputs") 
           or e.startswith(" External outputs") 
           or e.startswith(" Parameters")]
content = ''.join(content)

# remove comments
content = re.sub(r"/\*(.|\n)*?\*/", "", content)
print(content)
print("content=",content)
# remove all spaces around new lines and new lines
content = re.sub(r"\s*\n\s*", "", content)
# detect structure definition
# note: module "re" does not allow to detect repeted groups, so parsing the variables is done using the 'for' loop below
content1 = re.findall(r"(typedef struct\{((\w+ \w+(\[\d+\])*?;)+)\}(\w+);)", content)
# # remove new lines before '{'
# content = re.sub(r"\n\{", r" {", content)
# # add new lines after ";"
# content = re.sub(r";", r";\n", content) 
# # remove empty lines        
# content = re.sub(r"\n\s+\n", r"\n", content)  



def extract_content(vars, struct_name):
    variables_ = []
    kind = struct_name.split('_')[0]
    if "Ext" in kind:
        kind = kind[-1]  # special cases: ExtY, ExtU are 'Y' and 'U'

    vars = vars.strip()
    for row in vars.split(';'):
        if row:
            type_, name = row.split(' ')
            if '[' in name:   # variable is an array
                if str.count(name, '[') != 1:
                    raise NotImplementedError("Cas des arrays multidimensionnels non testé, vérifier l'implémentation actuelle.")
                name, other = name.split('[')
                length_ = other.split(']')[0]
                variable = [type_, name, length_]
            else:
                variable = [type_, name, None]
            variables_.append(variable)
    return variables_, kind

# several strings
variables = {}

for struct in content1:
    whole_struct, vars, *_, struct_name = struct
    variables_, kind = extract_content(vars, struct_name)
    variables[kind] = variables_

content2 = re.findall(r"(struct (\w+)\{((\w+ \w+(\[\d+\])*?;)+)\};)", content)
assert len(content2) == 1
for struct in content2:
    whole_struct, struct_name, vars, *_  = struct
    variables_, kind = extract_content(vars, struct_name)
    variables[kind] = variables_


# content = content.split('\n')
# variables = {}
# variables_ = []
# extract = False
# for row in content:
#     if row.startswith('typedef struct {'):
#         extract = True
#     elif row.startswith('}'):
#         if extract:
#             extract = False
#             kind = row.split(' ')[1].split('_')[0]
#             if "Ext" in kind:
#                 kind = kind[-1]  # special cases: ExtY, ExtU are 'Y' and 'U'
#             variables[kind] = variables_
#             variables_ = []
#         else:
#             break
#     else:
#         if extract:
#             # print("A")
#             # print(row)
#             row = row.strip()
#             row = row.split(';')[0]
#             # print(row.split(' '))
#             # print("B")
#             type_, name = row.split(' ')
#             if '[' in name:   # variable is an array
#                 name, other = name.split('[')
#                 length_ = other.split(']')[0]
#                 variable = [type_, name, length_]
#             else:
#                 variable = [type_, name, None]
#             variables_.append(variable)




# template: C code
def C_define_getter_array(kind, type_, name, length_):            # ajout de "kind" pour couvrir cas "name" identiques mais "kind" différent
    getter = \
f"""
void get{kind}_{name}({type_} (* {name}) []){{
    for (int i=0;i<{length_};i++){{
        (*{name})[i] = {model_name}_{kind}.{name}[i];
    }}
}}
"""
    return getter


def C_define_setter_array(kind, type_, name, length_):
    setter = \
f"""
void set{kind}_{name}({type_} (* {name}) []){{
    for (int i=0;i<{length_};i++){{
        model_name_{kind}.{name}[i] = (*{name})[i];
    }}
}}
"""
    return setter

def C_define_getter(kind, type_, name):
    getter = \
f"""
void get{kind}_{name}({type_} * {name}){{
        *{name} = {model_name}_{kind}.{name};
}}
"""
    return getter

def C_define_setter(kind, type_, name):
    setter = \
f"""
void set{kind}_{name}({type_} * {name}){{
        {model_name}_{kind}.{name} = *{name};
}}
"""
    return setter


getters = ["\n\n/* ======\nGETTERS\n=======*/\n\n"]
setters = ["\n\n/* ======\nSETTERS\n=======*/\n\n"]
for kind, variables_ in variables.items():
    # print(kind, variables_)
    getters.append(f"//-- {kind} --\n")
    setters.append(f"//-- {kind} --\n")
    for type_, name, length_ in variables_:
        if length_ is not None:  # array
            getter = C_define_getter_array(kind, type_, name, length_)
            setter = C_define_setter_array(kind, type_, name, length_)

        else:                    # scalar
            getter = C_define_getter(kind, type_, name)
            setter = C_define_setter(kind, type_, name)

        getters.append(getter)
        setters.append(setter)
        




content1 = ''.join(getters) + \
        ''.join(setters)

# ajout de la fonction d'initialisation
content2 = f"""
void initialize(int * stepSize0){{
  {model_name}_initialize();
  {model_name}_M->Timing.stepSize0 = *stepSize0;
}}
"""

c_code = content1 + content2

with open('code_interface.c', 'w') as f:
    f.writelines(c_code)



# template: Python code
def python_define_arg_types_array(kind, type_, name, length_):
    arg_types_ = \
f"""
lib.get{kind}_{name}.argtypes = (POINTER(c_double * {length_}), )
lib.set{kind}_{name}.argtypes = (POINTER(c_double * {length_}), )
"""
    return arg_types_


def python_define_arg_types(kind, type_, name):
    arg_types_ = \
f"""
lib.get{kind}_{name}.argtypes = (POINTER(c_double), )
lib.set{kind}_{name}.argtypes = (POINTER(c_double), )
"""
    return arg_types_



def python_define_getter_array(kind, type_, name, length_):
    getter = \
f"""
def get{kind}_{name}():
    {name} = (c_double * {length_})()
    lib.get{kind}_{name}(byref({name}))
    return tuple({name})
"""
    return getter


def python_define_setter_array(kind, type_, name, length_):
    setter = \
f"""
def set{kind}_{name}(values):
    {name} = (c_double * {length_})(*values)
    lib.set{kind}_{name}(byref({name}))
"""
    return setter


def python_define_getter(kind, type_, name):
    getter = \
f"""
def get{kind}_{name}():
    {name} = c_double()
    lib.get{kind}_{name}(byref({name}))
    return {name}.value
"""
    return getter

def python_define_setter(kind, type_, name):
    setter = \
f"""
def set{kind}_{name}(value):
    {name} = c_double(value)
    lib.set{kind}_{name}(byref({name}))
"""
    return setter



def python_define_getter_all(kind, variables_):
    function_list =  [f'get{kind}_{name}' for _, name, _ in variables_]
    function_list = str(function_list).replace("'", "")
    res = \
f"""
def get{kind}():
    res = tuple(func() for func in {function_list})
    return res
"""
    return res


def python_define_setter_all(kind, variables_):
    function_list =  [f'set{kind}_{name}' for _, name, _ in variables_]
    function_list = str(function_list).replace("'", "")
    res = \
f"""
def set{kind}(values):
    for values_, func in zip(values, {function_list}):
        func(values_)
"""
    return res

def python_define_mapper(kind, variables_):
    res = \
f"""
mapper_{kind} = {dict([[idx, name] for idx, (_, name, _) in enumerate(variables_)])}
"""
    return res

def python_define_description(kind, variables_):
    kind_descriptor = {'U': 'ENTREES', 'Y': 'SORTIES', 'P': 'PARAMETRES'}[kind]
    res = f'\n\n### {kind_descriptor}'
    if kind == 'P':
        res += "\n\n      obtenir la valeur actuelle: `getP_{nom_parametre}()`"
        res += "\n      changer de valeur: `setP_{nom_parametre}(valeur)`"
    else:
        res += "\n\n      voir pilotage"
    res += "\n"
    for idx, (type_, name, size) in enumerate(variables_):
        res += f"\n- {name}"
        res += f": itérable à {size} éléments" if size is not None else ""
    res = re.sub(r"\n", "\n# ", res) # mise en commentaires

    return res



arg_types = ["\n\n# =======\n# ARG TYPES\n# =======\n\n"]
getters = ["\n\n# =======\n# GETTERS\n# =======\n\n"]
setters = ["\n\n# =======\n# SETTERS\n# =======\n\n"]
mappers = ["\n\n# =======\n# MAPPERS\n# =======\n\n"]
descriptions = ['\npass']

for kind, variables_ in variables.items():
    # print(kind, variables_)
    arg_types.append(f"# -- {kind} --\n")
    getters.append(f"# -- {kind} --\n")
    setters.append(f"# -- {kind} --\n")
    mappers.append(f"# -- {kind} --\n")
    for type_, name, length_ in variables_:
        assert type_ == 'real_T'
        if length_ is not None:  # array
            arg_types_ = python_define_arg_types_array(kind, type_, name, length_)
            getter = python_define_getter_array(kind, type_, name, length_)
            setter = python_define_setter_array(kind, type_, name, length_)

        else:                    # scalar
            arg_types_ = python_define_arg_types(kind, type_, name)
            getter = python_define_getter(kind, type_, name)
            setter = python_define_setter(kind, type_, name)

        arg_types.append(arg_types_)
        getters.append(getter)
        setters.append(setter)


    getters.append(python_define_getter_all(kind, variables_))
    setters.append(python_define_setter_all(kind, variables_))
    mappers.append(python_define_mapper(kind, variables_))
    descriptions.append(python_define_description(kind, variables_))





# rassemblement de toutes les déclarations
# ajout de"if True" pour permettre le folding simplement

content1 = ''.join(arg_types) \
      +  ''.join(getters)      \
      +  ''.join(setters)         \
      +  ''.join(mappers) 
content1 = "\n\n # interface pour échange avec le code en C\nif True:\n" + re.sub(r"\n", "\n    ", content1)

# ajout de contenus avec leur propre "if True"
content2 = ''.join(descriptions)
content2 = "\n\n# liste des entrées, sorties et paramètres\nif True:\n" + re.sub(r"\n", "\n    ", content2)


# ajout de la fonction d'initialisation
content3 = """
lib.initialize.argtypes = (POINTER(c_int), )
def initialize(time_step: int):
    \"\"\"Initialise le modèle physique avec le pas de temps `time_step`.

    Parameters
    ----------
    time_step : int, secondes

    Notes
    -----
    Le pas de temps ne doit pas être régler en dehors de cette fonction
    \"\"\"
    stepSize0 = c_int(time_step)
    lib.initialize(byref(stepSize0))
"""
content3 = "\n\n# fonction d'initialisation pour réglage du pas de temps: à appeler en tout début de script\nif True:\n" + re.sub(r"\n", "\n    ", content3)

python_code = content1 + content2 + content3
with open('code_interface.py', 'w') as f:
    f.writelines(python_code)


