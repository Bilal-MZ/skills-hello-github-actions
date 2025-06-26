from ctypes import *
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.optimize import minimize
import tqdm
from time import sleep

lib_path = r'/home/mouzounb/Bureau/parallel_ECS_stock_aval/Code_C/parallele_ECS_Stock_aval_ert_rtw/liball.so'


from ctypes import *
lib = cdll.LoadLibrary(lib_path)   


import matplotlib as mpl
mpl.rcParams['date.autoformatter.hour'] = '%d %b %Hh'
mpl.rcParams['date.autoformatter.minute'] = '%d %b %H:%M'














 

 # interface pour échange avec le code en C
if True:

    
    # =======
    # ARG TYPES
    # =======
    
    # -- U --
    
    lib.getU_m_ch_dir.argtypes = (POINTER(c_double), )
    lib.setU_m_ch_dir.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_sout.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_sout.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_stock.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_stock.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_sec.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_sec.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ch_V3V.argtypes = (POINTER(c_double), )
    lib.setU_m_ch_V3V.argtypes = (POINTER(c_double), )
    
    lib.getU_m_prim.argtypes = (POINTER(c_double), )
    lib.setU_m_prim.argtypes = (POINTER(c_double), )
    
    lib.getU_T_prim_in.argtypes = (POINTER(c_double), )
    lib.setU_T_prim_in.argtypes = (POINTER(c_double), )
    
    lib.getU_T_edv.argtypes = (POINTER(c_double), )
    lib.setU_T_edv.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_dir.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_dir.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_V3V.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_V3V.argtypes = (POINTER(c_double), )
    
    lib.getU_m_ECS_bouc.argtypes = (POINTER(c_double), )
    lib.setU_m_ECS_bouc.argtypes = (POINTER(c_double), )
    # -- Y --
    
    lib.getY_T_sec_in.argtypes = (POINTER(c_double), )
    lib.setY_T_sec_in.argtypes = (POINTER(c_double), )
    
    lib.getY_T_out_ECS.argtypes = (POINTER(c_double), )
    lib.setY_T_out_ECS.argtypes = (POINTER(c_double), )
    
    lib.getY_T_out.argtypes = (POINTER(c_double), )
    lib.setY_T_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_sec_out.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_sec_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_sec_in.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_sec_in.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_prim_in.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_prim_in.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_prim_out.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_prim_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ch_out.argtypes = (POINTER(c_double), )
    lib.setY_T_ch_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ch_in.argtypes = (POINTER(c_double), )
    lib.setY_T_ch_in.argtypes = (POINTER(c_double), )
    
    lib.getY_T_prim_out.argtypes = (POINTER(c_double), )
    lib.setY_T_prim_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_sec_out.argtypes = (POINTER(c_double), )
    lib.setY_T_sec_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_out_emetteur.argtypes = (POINTER(c_double), )
    lib.setY_T_out_emetteur.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_n.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_n.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_ch.argtypes = (POINTER(c_double), )
    lib.setY_Q_ch.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_ech.argtypes = (POINTER(c_double), )
    lib.setY_Q_ech.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_ech_ECS.argtypes = (POINTER(c_double), )
    lib.setY_Q_ech_ECS.argtypes = (POINTER(c_double), )
    
    lib.getY_m_ECS.argtypes = (POINTER(c_double), )
    lib.setY_m_ECS.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_aller.argtypes = (POINTER(c_double), )
    lib.setY_Q_aller.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_retour.argtypes = (POINTER(c_double), )
    lib.setY_Q_retour.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ballon_out.argtypes = (POINTER(c_double), )
    lib.setY_T_ballon_out.argtypes = (POINTER(c_double), )
    
    lib.getY_T_avg.argtypes = (POINTER(c_double), )
    lib.setY_T_avg.argtypes = (POINTER(c_double), )
    
    lib.getY_T_mid.argtypes = (POINTER(c_double), )
    lib.setY_T_mid.argtypes = (POINTER(c_double), )
    
    lib.getY_T_std.argtypes = (POINTER(c_double), )
    lib.setY_T_std.argtypes = (POINTER(c_double), )
    
    lib.getY_T_half.argtypes = (POINTER(c_double), )
    lib.setY_T_half.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_1.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_1.argtypes = (POINTER(c_double), )
    
    lib.getY_m_ECS_prim.argtypes = (POINTER(c_double), )
    lib.setY_m_ECS_prim.argtypes = (POINTER(c_double), )
    
    lib.getY_m_sec.argtypes = (POINTER(c_double), )
    lib.setY_m_sec.argtypes = (POINTER(c_double), )
    
    lib.getY_m_ch.argtypes = (POINTER(c_double), )
    lib.setY_m_ch.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_ECS_aller.argtypes = (POINTER(c_double), )
    lib.setY_Q_ECS_aller.argtypes = (POINTER(c_double), )
    
    lib.getY_Q_ECS_retour.argtypes = (POINTER(c_double), )
    lib.setY_Q_ECS_retour.argtypes = (POINTER(c_double), )
    
    lib.getY_eff_ech.argtypes = (POINTER(c_double), )
    lib.setY_eff_ech.argtypes = (POINTER(c_double), )
    
    lib.getY_eff_ech_ECS.argtypes = (POINTER(c_double), )
    lib.setY_eff_ech_ECS.argtypes = (POINTER(c_double), )
    
    lib.getY_m_2_ree.argtypes = (POINTER(c_double), )
    lib.setY_m_2_ree.argtypes = (POINTER(c_double), )
    
    lib.getY_T_ECS_in.argtypes = (POINTER(c_double), )
    lib.setY_T_ECS_in.argtypes = (POINTER(c_double), )
    
    lib.getY_T_in_emet.argtypes = (POINTER(c_double), )
    lib.setY_T_in_emet.argtypes = (POINTER(c_double), )
    # -- P --
    
    lib.getP_Ballondestockage_D.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_D.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffagealler_D.argtypes = (POINTER(c_double), )
    lib.setP_Chauffagealler_D.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffageretour_D.argtypes = (POINTER(c_double), )
    lib.setP_Chauffageretour_D.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSaller_D.argtypes = (POINTER(c_double), )
    lib.setP_ECSaller_D.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSretour_D.argtypes = (POINTER(c_double), )
    lib.setP_ECSretour_D.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_D.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_D.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_H.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_H.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffagealler_L.argtypes = (POINTER(c_double), )
    lib.setP_Chauffagealler_L.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffageretour_L.argtypes = (POINTER(c_double), )
    lib.setP_Chauffageretour_L.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSaller_L.argtypes = (POINTER(c_double), )
    lib.setP_ECSaller_L.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSretour_L.argtypes = (POINTER(c_double), )
    lib.setP_ECSretour_L.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_L.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_L.argtypes = (POINTER(c_double), )
    
    lib.getP_Echangeurrseau_S.argtypes = (POINTER(c_double), )
    lib.setP_Echangeurrseau_S.argtypes = (POINTER(c_double), )
    
    lib.getP_EchangeurECS_S.argtypes = (POINTER(c_double), )
    lib.setP_EchangeurECS_S.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_T_air.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_T_air.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_T_amb.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_T_amb.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffagealler_T_local.argtypes = (POINTER(c_double), )
    lib.setP_Chauffagealler_T_local.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffageretour_T_local.argtypes = (POINTER(c_double), )
    lib.setP_Chauffageretour_T_local.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSaller_T_local.argtypes = (POINTER(c_double), )
    lib.setP_ECSaller_T_local.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSretour_T_local.argtypes = (POINTER(c_double), )
    lib.setP_ECSretour_T_local.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_U.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_U.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_U.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_U.argtypes = (POINTER(c_double), )
    
    lib.getP_Echangeurrseau_U.argtypes = (POINTER(c_double), )
    lib.setP_Echangeurrseau_U.argtypes = (POINTER(c_double), )
    
    lib.getP_EchangeurECS_U.argtypes = (POINTER(c_double), )
    lib.setP_EchangeurECS_U.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_V_min.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_V_min.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_V_var.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_V_var.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_eps.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_eps.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffagealler_m_min.argtypes = (POINTER(c_double), )
    lib.setP_Chauffagealler_m_min.argtypes = (POINTER(c_double), )
    
    lib.getP_Chauffageretour_m_min.argtypes = (POINTER(c_double), )
    lib.setP_Chauffageretour_m_min.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSaller_m_min.argtypes = (POINTER(c_double), )
    lib.setP_ECSaller_m_min.argtypes = (POINTER(c_double), )
    
    lib.getP_ECSretour_m_min.argtypes = (POINTER(c_double), )
    lib.setP_ECSretour_m_min.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_m_min.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_m_min.argtypes = (POINTER(c_double), )
    
    lib.getP_Ballondestockage_n.argtypes = (POINTER(c_double), )
    lib.setP_Ballondestockage_n.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_n_radiateurs.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_n_radiateurs.argtypes = (POINTER(c_double), )
    
    lib.getP_emetteurs_n_tubes.argtypes = (POINTER(c_double), )
    lib.setP_emetteurs_n_tubes.argtypes = (POINTER(c_double), )
    
    lib.getP_DelayRoot2_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_DelayRoot2_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_DelayRoot3_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_DelayRoot3_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Constant1_Value.argtypes = (POINTER(c_double), )
    lib.setP_Constant1_Value.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_l.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_l.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_j.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_j.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay1_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay1_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Constant17_Value.argtypes = (POINTER(c_double), )
    lib.setP_Constant17_Value.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_o.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_o.argtypes = (POINTER(c_double), )
    
    lib.getP_Constant24_Value.argtypes = (POINTER(c_double), )
    lib.setP_Constant24_Value.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay2_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay2_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay3_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay3_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay5_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay5_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay4_InitialCondition.argtypes = (POINTER(c_double), )
    lib.setP_Delay4_InitialCondition.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_o3.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_o3.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_k.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_k.argtypes = (POINTER(c_double), )
    
    lib.getP_Switch_Threshold.argtypes = (POINTER(c_double), )
    lib.setP_Switch_Threshold.argtypes = (POINTER(c_double), )
    
    lib.getP_Delay_InitialCondition_o4.argtypes = (POINTER(c_double), )
    lib.setP_Delay_InitialCondition_o4.argtypes = (POINTER(c_double), )
    
    lib.getP_Constant25_Value.argtypes = (POINTER(c_double), )
    lib.setP_Constant25_Value.argtypes = (POINTER(c_double), )
    
    lib.getP_Constant26_Value.argtypes = (POINTER(c_double), )
    lib.setP_Constant26_Value.argtypes = (POINTER(c_double), )
    
    lib.getP_Gain_Gain.argtypes = (POINTER(c_double), )
    lib.setP_Gain_Gain.argtypes = (POINTER(c_double), )
    
    
    # =======
    # GETTERS
    # =======
    
    # -- U --
    
    def getU_m_ch_dir():
        m_ch_dir = c_double()
        lib.getU_m_ch_dir(byref(m_ch_dir))
        return m_ch_dir.value
    
    def getU_m_ECS_sout():
        m_ECS_sout = c_double()
        lib.getU_m_ECS_sout(byref(m_ECS_sout))
        return m_ECS_sout.value
    
    def getU_m_ECS_stock():
        m_ECS_stock = c_double()
        lib.getU_m_ECS_stock(byref(m_ECS_stock))
        return m_ECS_stock.value
    
    def getU_m_ECS_sec():
        m_ECS_sec = c_double()
        lib.getU_m_ECS_sec(byref(m_ECS_sec))
        return m_ECS_sec.value
    
    def getU_m_ch_V3V():
        m_ch_V3V = c_double()
        lib.getU_m_ch_V3V(byref(m_ch_V3V))
        return m_ch_V3V.value
    
    def getU_m_prim():
        m_prim = c_double()
        lib.getU_m_prim(byref(m_prim))
        return m_prim.value
    
    def getU_T_prim_in():
        T_prim_in = c_double()
        lib.getU_T_prim_in(byref(T_prim_in))
        return T_prim_in.value
    
    def getU_T_edv():
        T_edv = c_double()
        lib.getU_T_edv(byref(T_edv))
        return T_edv.value
    
    def getU_m_ECS_dir():
        m_ECS_dir = c_double()
        lib.getU_m_ECS_dir(byref(m_ECS_dir))
        return m_ECS_dir.value
    
    def getU_m_ECS_V3V():
        m_ECS_V3V = c_double()
        lib.getU_m_ECS_V3V(byref(m_ECS_V3V))
        return m_ECS_V3V.value
    
    def getU_m_ECS_bouc():
        m_ECS_bouc = c_double()
        lib.getU_m_ECS_bouc(byref(m_ECS_bouc))
        return m_ECS_bouc.value
    
    def getU():
        res = tuple(func() for func in [getU_m_ch_dir, getU_m_ECS_sout, getU_m_ECS_stock, getU_m_ECS_sec, getU_m_ch_V3V, getU_m_prim, getU_T_prim_in, getU_T_edv, getU_m_ECS_dir, getU_m_ECS_V3V, getU_m_ECS_bouc])
        return res
    # -- Y --
    
    def getY_T_sec_in():
        T_sec_in = c_double()
        lib.getY_T_sec_in(byref(T_sec_in))
        return T_sec_in.value
    
    def getY_T_out_ECS():
        T_out_ECS = c_double()
        lib.getY_T_out_ECS(byref(T_out_ECS))
        return T_out_ECS.value
    
    def getY_T_out():
        T_out = c_double()
        lib.getY_T_out(byref(T_out))
        return T_out.value
    
    def getY_T_ECS_sec_out():
        T_ECS_sec_out = c_double()
        lib.getY_T_ECS_sec_out(byref(T_ECS_sec_out))
        return T_ECS_sec_out.value
    
    def getY_T_ECS_sec_in():
        T_ECS_sec_in = c_double()
        lib.getY_T_ECS_sec_in(byref(T_ECS_sec_in))
        return T_ECS_sec_in.value
    
    def getY_T_ECS_prim_in():
        T_ECS_prim_in = c_double()
        lib.getY_T_ECS_prim_in(byref(T_ECS_prim_in))
        return T_ECS_prim_in.value
    
    def getY_T_ECS_prim_out():
        T_ECS_prim_out = c_double()
        lib.getY_T_ECS_prim_out(byref(T_ECS_prim_out))
        return T_ECS_prim_out.value
    
    def getY_T_ch_out():
        T_ch_out = c_double()
        lib.getY_T_ch_out(byref(T_ch_out))
        return T_ch_out.value
    
    def getY_T_ch_in():
        T_ch_in = c_double()
        lib.getY_T_ch_in(byref(T_ch_in))
        return T_ch_in.value
    
    def getY_T_prim_out():
        T_prim_out = c_double()
        lib.getY_T_prim_out(byref(T_prim_out))
        return T_prim_out.value
    
    def getY_T_sec_out():
        T_sec_out = c_double()
        lib.getY_T_sec_out(byref(T_sec_out))
        return T_sec_out.value
    
    def getY_T_out_emetteur():
        T_out_emetteur = c_double()
        lib.getY_T_out_emetteur(byref(T_out_emetteur))
        return T_out_emetteur.value
    
    def getY_T_ECS_n():
        T_ECS_n = c_double()
        lib.getY_T_ECS_n(byref(T_ECS_n))
        return T_ECS_n.value
    
    def getY_Q_ch():
        Q_ch = c_double()
        lib.getY_Q_ch(byref(Q_ch))
        return Q_ch.value
    
    def getY_Q_ech():
        Q_ech = c_double()
        lib.getY_Q_ech(byref(Q_ech))
        return Q_ech.value
    
    def getY_Q_ech_ECS():
        Q_ech_ECS = c_double()
        lib.getY_Q_ech_ECS(byref(Q_ech_ECS))
        return Q_ech_ECS.value
    
    def getY_m_ECS():
        m_ECS = c_double()
        lib.getY_m_ECS(byref(m_ECS))
        return m_ECS.value
    
    def getY_Q_aller():
        Q_aller = c_double()
        lib.getY_Q_aller(byref(Q_aller))
        return Q_aller.value
    
    def getY_Q_retour():
        Q_retour = c_double()
        lib.getY_Q_retour(byref(Q_retour))
        return Q_retour.value
    
    def getY_T_ballon_out():
        T_ballon_out = c_double()
        lib.getY_T_ballon_out(byref(T_ballon_out))
        return T_ballon_out.value
    
    def getY_T_avg():
        T_avg = c_double()
        lib.getY_T_avg(byref(T_avg))
        return T_avg.value
    
    def getY_T_mid():
        T_mid = c_double()
        lib.getY_T_mid(byref(T_mid))
        return T_mid.value
    
    def getY_T_std():
        T_std = c_double()
        lib.getY_T_std(byref(T_std))
        return T_std.value
    
    def getY_T_half():
        T_half = c_double()
        lib.getY_T_half(byref(T_half))
        return T_half.value
    
    def getY_T_ECS_1():
        T_ECS_1 = c_double()
        lib.getY_T_ECS_1(byref(T_ECS_1))
        return T_ECS_1.value
    
    def getY_m_ECS_prim():
        m_ECS_prim = c_double()
        lib.getY_m_ECS_prim(byref(m_ECS_prim))
        return m_ECS_prim.value
    
    def getY_m_sec():
        m_sec = c_double()
        lib.getY_m_sec(byref(m_sec))
        return m_sec.value
    
    def getY_m_ch():
        m_ch = c_double()
        lib.getY_m_ch(byref(m_ch))
        return m_ch.value
    
    def getY_Q_ECS_aller():
        Q_ECS_aller = c_double()
        lib.getY_Q_ECS_aller(byref(Q_ECS_aller))
        return Q_ECS_aller.value
    
    def getY_Q_ECS_retour():
        Q_ECS_retour = c_double()
        lib.getY_Q_ECS_retour(byref(Q_ECS_retour))
        return Q_ECS_retour.value
    
    def getY_eff_ech():
        eff_ech = c_double()
        lib.getY_eff_ech(byref(eff_ech))
        return eff_ech.value
    
    def getY_eff_ech_ECS():
        eff_ech_ECS = c_double()
        lib.getY_eff_ech_ECS(byref(eff_ech_ECS))
        return eff_ech_ECS.value
    
    def getY_m_2_ree():
        m_2_ree = c_double()
        lib.getY_m_2_ree(byref(m_2_ree))
        return m_2_ree.value
    
    def getY_T_ECS_in():
        T_ECS_in = c_double()
        lib.getY_T_ECS_in(byref(T_ECS_in))
        return T_ECS_in.value
    
    def getY_T_in_emet():
        T_in_emet = c_double()
        lib.getY_T_in_emet(byref(T_in_emet))
        return T_in_emet.value
    
    def getY():
        res = tuple(func() for func in [getY_T_sec_in, getY_T_out_ECS, getY_T_out, getY_T_ECS_sec_out, getY_T_ECS_sec_in, getY_T_ECS_prim_in, getY_T_ECS_prim_out, getY_T_ch_out, getY_T_ch_in, getY_T_prim_out, getY_T_sec_out, getY_T_out_emetteur, getY_T_ECS_n, getY_Q_ch, getY_Q_ech, getY_Q_ech_ECS, getY_m_ECS, getY_Q_aller, getY_Q_retour, getY_T_ballon_out, getY_T_avg, getY_T_mid, getY_T_std, getY_T_half, getY_T_ECS_1, getY_m_ECS_prim, getY_m_sec, getY_m_ch, getY_Q_ECS_aller, getY_Q_ECS_retour, getY_eff_ech, getY_eff_ech_ECS, getY_m_2_ree, getY_T_ECS_in, getY_T_in_emet])
        return res
    # -- P --
    
    def getP_Ballondestockage_D():
        Ballondestockage_D = c_double()
        lib.getP_Ballondestockage_D(byref(Ballondestockage_D))
        return Ballondestockage_D.value
    
    def getP_Chauffagealler_D():
        Chauffagealler_D = c_double()
        lib.getP_Chauffagealler_D(byref(Chauffagealler_D))
        return Chauffagealler_D.value
    
    def getP_Chauffageretour_D():
        Chauffageretour_D = c_double()
        lib.getP_Chauffageretour_D(byref(Chauffageretour_D))
        return Chauffageretour_D.value
    
    def getP_ECSaller_D():
        ECSaller_D = c_double()
        lib.getP_ECSaller_D(byref(ECSaller_D))
        return ECSaller_D.value
    
    def getP_ECSretour_D():
        ECSretour_D = c_double()
        lib.getP_ECSretour_D(byref(ECSretour_D))
        return ECSretour_D.value
    
    def getP_emetteurs_D():
        emetteurs_D = c_double()
        lib.getP_emetteurs_D(byref(emetteurs_D))
        return emetteurs_D.value
    
    def getP_Ballondestockage_H():
        Ballondestockage_H = c_double()
        lib.getP_Ballondestockage_H(byref(Ballondestockage_H))
        return Ballondestockage_H.value
    
    def getP_Chauffagealler_L():
        Chauffagealler_L = c_double()
        lib.getP_Chauffagealler_L(byref(Chauffagealler_L))
        return Chauffagealler_L.value
    
    def getP_Chauffageretour_L():
        Chauffageretour_L = c_double()
        lib.getP_Chauffageretour_L(byref(Chauffageretour_L))
        return Chauffageretour_L.value
    
    def getP_ECSaller_L():
        ECSaller_L = c_double()
        lib.getP_ECSaller_L(byref(ECSaller_L))
        return ECSaller_L.value
    
    def getP_ECSretour_L():
        ECSretour_L = c_double()
        lib.getP_ECSretour_L(byref(ECSretour_L))
        return ECSretour_L.value
    
    def getP_emetteurs_L():
        emetteurs_L = c_double()
        lib.getP_emetteurs_L(byref(emetteurs_L))
        return emetteurs_L.value
    
    def getP_Echangeurrseau_S():
        Echangeurrseau_S = c_double()
        lib.getP_Echangeurrseau_S(byref(Echangeurrseau_S))
        return Echangeurrseau_S.value
    
    def getP_EchangeurECS_S():
        EchangeurECS_S = c_double()
        lib.getP_EchangeurECS_S(byref(EchangeurECS_S))
        return EchangeurECS_S.value
    
    def getP_emetteurs_T_air():
        emetteurs_T_air = c_double()
        lib.getP_emetteurs_T_air(byref(emetteurs_T_air))
        return emetteurs_T_air.value
    
    def getP_Ballondestockage_T_amb():
        Ballondestockage_T_amb = c_double()
        lib.getP_Ballondestockage_T_amb(byref(Ballondestockage_T_amb))
        return Ballondestockage_T_amb.value
    
    def getP_Chauffagealler_T_local():
        Chauffagealler_T_local = c_double()
        lib.getP_Chauffagealler_T_local(byref(Chauffagealler_T_local))
        return Chauffagealler_T_local.value
    
    def getP_Chauffageretour_T_local():
        Chauffageretour_T_local = c_double()
        lib.getP_Chauffageretour_T_local(byref(Chauffageretour_T_local))
        return Chauffageretour_T_local.value
    
    def getP_ECSaller_T_local():
        ECSaller_T_local = c_double()
        lib.getP_ECSaller_T_local(byref(ECSaller_T_local))
        return ECSaller_T_local.value
    
    def getP_ECSretour_T_local():
        ECSretour_T_local = c_double()
        lib.getP_ECSretour_T_local(byref(ECSretour_T_local))
        return ECSretour_T_local.value
    
    def getP_Ballondestockage_U():
        Ballondestockage_U = c_double()
        lib.getP_Ballondestockage_U(byref(Ballondestockage_U))
        return Ballondestockage_U.value
    
    def getP_emetteurs_U():
        emetteurs_U = c_double()
        lib.getP_emetteurs_U(byref(emetteurs_U))
        return emetteurs_U.value
    
    def getP_Echangeurrseau_U():
        Echangeurrseau_U = c_double()
        lib.getP_Echangeurrseau_U(byref(Echangeurrseau_U))
        return Echangeurrseau_U.value
    
    def getP_EchangeurECS_U():
        EchangeurECS_U = c_double()
        lib.getP_EchangeurECS_U(byref(EchangeurECS_U))
        return EchangeurECS_U.value
    
    def getP_Ballondestockage_V_min():
        Ballondestockage_V_min = c_double()
        lib.getP_Ballondestockage_V_min(byref(Ballondestockage_V_min))
        return Ballondestockage_V_min.value
    
    def getP_Ballondestockage_V_var():
        Ballondestockage_V_var = c_double()
        lib.getP_Ballondestockage_V_var(byref(Ballondestockage_V_var))
        return Ballondestockage_V_var.value
    
    def getP_Ballondestockage_eps():
        Ballondestockage_eps = c_double()
        lib.getP_Ballondestockage_eps(byref(Ballondestockage_eps))
        return Ballondestockage_eps.value
    
    def getP_Chauffagealler_m_min():
        Chauffagealler_m_min = c_double()
        lib.getP_Chauffagealler_m_min(byref(Chauffagealler_m_min))
        return Chauffagealler_m_min.value
    
    def getP_Chauffageretour_m_min():
        Chauffageretour_m_min = c_double()
        lib.getP_Chauffageretour_m_min(byref(Chauffageretour_m_min))
        return Chauffageretour_m_min.value
    
    def getP_ECSaller_m_min():
        ECSaller_m_min = c_double()
        lib.getP_ECSaller_m_min(byref(ECSaller_m_min))
        return ECSaller_m_min.value
    
    def getP_ECSretour_m_min():
        ECSretour_m_min = c_double()
        lib.getP_ECSretour_m_min(byref(ECSretour_m_min))
        return ECSretour_m_min.value
    
    def getP_emetteurs_m_min():
        emetteurs_m_min = c_double()
        lib.getP_emetteurs_m_min(byref(emetteurs_m_min))
        return emetteurs_m_min.value
    
    def getP_Ballondestockage_n():
        Ballondestockage_n = c_double()
        lib.getP_Ballondestockage_n(byref(Ballondestockage_n))
        return Ballondestockage_n.value
    
    def getP_emetteurs_n_radiateurs():
        emetteurs_n_radiateurs = c_double()
        lib.getP_emetteurs_n_radiateurs(byref(emetteurs_n_radiateurs))
        return emetteurs_n_radiateurs.value
    
    def getP_emetteurs_n_tubes():
        emetteurs_n_tubes = c_double()
        lib.getP_emetteurs_n_tubes(byref(emetteurs_n_tubes))
        return emetteurs_n_tubes.value
    
    def getP_DelayRoot2_InitialCondition():
        DelayRoot2_InitialCondition = c_double()
        lib.getP_DelayRoot2_InitialCondition(byref(DelayRoot2_InitialCondition))
        return DelayRoot2_InitialCondition.value
    
    def getP_DelayRoot3_InitialCondition():
        DelayRoot3_InitialCondition = c_double()
        lib.getP_DelayRoot3_InitialCondition(byref(DelayRoot3_InitialCondition))
        return DelayRoot3_InitialCondition.value
    
    def getP_Constant1_Value():
        Constant1_Value = c_double()
        lib.getP_Constant1_Value(byref(Constant1_Value))
        return Constant1_Value.value
    
    def getP_Delay_InitialCondition():
        Delay_InitialCondition = c_double()
        lib.getP_Delay_InitialCondition(byref(Delay_InitialCondition))
        return Delay_InitialCondition.value
    
    def getP_Delay_InitialCondition_l():
        Delay_InitialCondition_l = c_double()
        lib.getP_Delay_InitialCondition_l(byref(Delay_InitialCondition_l))
        return Delay_InitialCondition_l.value
    
    def getP_Delay_InitialCondition_j():
        Delay_InitialCondition_j = c_double()
        lib.getP_Delay_InitialCondition_j(byref(Delay_InitialCondition_j))
        return Delay_InitialCondition_j.value
    
    def getP_Delay1_InitialCondition():
        Delay1_InitialCondition = c_double()
        lib.getP_Delay1_InitialCondition(byref(Delay1_InitialCondition))
        return Delay1_InitialCondition.value
    
    def getP_Constant17_Value():
        Constant17_Value = c_double()
        lib.getP_Constant17_Value(byref(Constant17_Value))
        return Constant17_Value.value
    
    def getP_Delay_InitialCondition_o():
        Delay_InitialCondition_o = c_double()
        lib.getP_Delay_InitialCondition_o(byref(Delay_InitialCondition_o))
        return Delay_InitialCondition_o.value
    
    def getP_Constant24_Value():
        Constant24_Value = c_double()
        lib.getP_Constant24_Value(byref(Constant24_Value))
        return Constant24_Value.value
    
    def getP_Delay2_InitialCondition():
        Delay2_InitialCondition = c_double()
        lib.getP_Delay2_InitialCondition(byref(Delay2_InitialCondition))
        return Delay2_InitialCondition.value
    
    def getP_Delay3_InitialCondition():
        Delay3_InitialCondition = c_double()
        lib.getP_Delay3_InitialCondition(byref(Delay3_InitialCondition))
        return Delay3_InitialCondition.value
    
    def getP_Delay5_InitialCondition():
        Delay5_InitialCondition = c_double()
        lib.getP_Delay5_InitialCondition(byref(Delay5_InitialCondition))
        return Delay5_InitialCondition.value
    
    def getP_Delay4_InitialCondition():
        Delay4_InitialCondition = c_double()
        lib.getP_Delay4_InitialCondition(byref(Delay4_InitialCondition))
        return Delay4_InitialCondition.value
    
    def getP_Delay_InitialCondition_o3():
        Delay_InitialCondition_o3 = c_double()
        lib.getP_Delay_InitialCondition_o3(byref(Delay_InitialCondition_o3))
        return Delay_InitialCondition_o3.value
    
    def getP_Delay_InitialCondition_k():
        Delay_InitialCondition_k = c_double()
        lib.getP_Delay_InitialCondition_k(byref(Delay_InitialCondition_k))
        return Delay_InitialCondition_k.value
    
    def getP_Switch_Threshold():
        Switch_Threshold = c_double()
        lib.getP_Switch_Threshold(byref(Switch_Threshold))
        return Switch_Threshold.value
    
    def getP_Delay_InitialCondition_o4():
        Delay_InitialCondition_o4 = c_double()
        lib.getP_Delay_InitialCondition_o4(byref(Delay_InitialCondition_o4))
        return Delay_InitialCondition_o4.value
    
    def getP_Constant25_Value():
        Constant25_Value = c_double()
        lib.getP_Constant25_Value(byref(Constant25_Value))
        return Constant25_Value.value
    
    def getP_Constant26_Value():
        Constant26_Value = c_double()
        lib.getP_Constant26_Value(byref(Constant26_Value))
        return Constant26_Value.value
    
    def getP_Gain_Gain():
        Gain_Gain = c_double()
        lib.getP_Gain_Gain(byref(Gain_Gain))
        return Gain_Gain.value
    
    def getP():
        res = tuple(func() for func in [getP_Ballondestockage_D, getP_Chauffagealler_D, getP_Chauffageretour_D, getP_ECSaller_D, getP_ECSretour_D, getP_emetteurs_D, getP_Ballondestockage_H, getP_Chauffagealler_L, getP_Chauffageretour_L, getP_ECSaller_L, getP_ECSretour_L, getP_emetteurs_L, getP_Echangeurrseau_S, getP_EchangeurECS_S, getP_emetteurs_T_air, getP_Ballondestockage_T_amb, getP_Chauffagealler_T_local, getP_Chauffageretour_T_local, getP_ECSaller_T_local, getP_ECSretour_T_local, getP_Ballondestockage_U, getP_emetteurs_U, getP_Echangeurrseau_U, getP_EchangeurECS_U, getP_Ballondestockage_V_min, getP_Ballondestockage_V_var, getP_Ballondestockage_eps, getP_Chauffagealler_m_min, getP_Chauffageretour_m_min, getP_ECSaller_m_min, getP_ECSretour_m_min, getP_emetteurs_m_min, getP_Ballondestockage_n, getP_emetteurs_n_radiateurs, getP_emetteurs_n_tubes, getP_DelayRoot2_InitialCondition, getP_DelayRoot3_InitialCondition, getP_Constant1_Value, getP_Delay_InitialCondition, getP_Delay_InitialCondition_l, getP_Delay_InitialCondition_j, getP_Delay1_InitialCondition, getP_Constant17_Value, getP_Delay_InitialCondition_o, getP_Constant24_Value, getP_Delay2_InitialCondition, getP_Delay3_InitialCondition, getP_Delay5_InitialCondition, getP_Delay4_InitialCondition, getP_Delay_InitialCondition_o3, getP_Delay_InitialCondition_k, getP_Switch_Threshold, getP_Delay_InitialCondition_o4, getP_Constant25_Value, getP_Constant26_Value, getP_Gain_Gain])
        return res
    
    
    # =======
    # SETTERS
    # =======
    
    # -- U --
    
    def setU_m_ch_dir(value):
        m_ch_dir = c_double(value)
        lib.setU_m_ch_dir(byref(m_ch_dir))
    
    def setU_m_ECS_sout(value):
        m_ECS_sout = c_double(value)
        lib.setU_m_ECS_sout(byref(m_ECS_sout))
    
    def setU_m_ECS_stock(value):
        m_ECS_stock = c_double(value)
        lib.setU_m_ECS_stock(byref(m_ECS_stock))
    
    def setU_m_ECS_sec(value):
        m_ECS_sec = c_double(value)
        lib.setU_m_ECS_sec(byref(m_ECS_sec))
    
    def setU_m_ch_V3V(value):
        m_ch_V3V = c_double(value)
        lib.setU_m_ch_V3V(byref(m_ch_V3V))
    
    def setU_m_prim(value):
        m_prim = c_double(value)
        lib.setU_m_prim(byref(m_prim))
    
    def setU_T_prim_in(value):
        T_prim_in = c_double(value)
        lib.setU_T_prim_in(byref(T_prim_in))
    
    def setU_T_edv(value):
        T_edv = c_double(value)
        lib.setU_T_edv(byref(T_edv))
    
    def setU_m_ECS_dir(value):
        m_ECS_dir = c_double(value)
        lib.setU_m_ECS_dir(byref(m_ECS_dir))
    
    def setU_m_ECS_V3V(value):
        m_ECS_V3V = c_double(value)
        lib.setU_m_ECS_V3V(byref(m_ECS_V3V))
    
    def setU_m_ECS_bouc(value):
        m_ECS_bouc = c_double(value)
        lib.setU_m_ECS_bouc(byref(m_ECS_bouc))
    
    def setU(values):
        for values_, func in zip(values, [setU_m_ch_dir, setU_m_ECS_sout, setU_m_ECS_stock, setU_m_ECS_sec, setU_m_ch_V3V, setU_m_prim, setU_T_prim_in, setU_T_edv, setU_m_ECS_dir, setU_m_ECS_V3V, setU_m_ECS_bouc]):
            func(values_)
    # -- Y --
    
    def setY_T_sec_in(value):
        T_sec_in = c_double(value)
        lib.setY_T_sec_in(byref(T_sec_in))
    
    def setY_T_out_ECS(value):
        T_out_ECS = c_double(value)
        lib.setY_T_out_ECS(byref(T_out_ECS))
    
    def setY_T_out(value):
        T_out = c_double(value)
        lib.setY_T_out(byref(T_out))
    
    def setY_T_ECS_sec_out(value):
        T_ECS_sec_out = c_double(value)
        lib.setY_T_ECS_sec_out(byref(T_ECS_sec_out))
    
    def setY_T_ECS_sec_in(value):
        T_ECS_sec_in = c_double(value)
        lib.setY_T_ECS_sec_in(byref(T_ECS_sec_in))
    
    def setY_T_ECS_prim_in(value):
        T_ECS_prim_in = c_double(value)
        lib.setY_T_ECS_prim_in(byref(T_ECS_prim_in))
    
    def setY_T_ECS_prim_out(value):
        T_ECS_prim_out = c_double(value)
        lib.setY_T_ECS_prim_out(byref(T_ECS_prim_out))
    
    def setY_T_ch_out(value):
        T_ch_out = c_double(value)
        lib.setY_T_ch_out(byref(T_ch_out))
    
    def setY_T_ch_in(value):
        T_ch_in = c_double(value)
        lib.setY_T_ch_in(byref(T_ch_in))
    
    def setY_T_prim_out(value):
        T_prim_out = c_double(value)
        lib.setY_T_prim_out(byref(T_prim_out))
    
    def setY_T_sec_out(value):
        T_sec_out = c_double(value)
        lib.setY_T_sec_out(byref(T_sec_out))
    
    def setY_T_out_emetteur(value):
        T_out_emetteur = c_double(value)
        lib.setY_T_out_emetteur(byref(T_out_emetteur))
    
    def setY_T_ECS_n(value):
        T_ECS_n = c_double(value)
        lib.setY_T_ECS_n(byref(T_ECS_n))
    
    def setY_Q_ch(value):
        Q_ch = c_double(value)
        lib.setY_Q_ch(byref(Q_ch))
    
    def setY_Q_ech(value):
        Q_ech = c_double(value)
        lib.setY_Q_ech(byref(Q_ech))
    
    def setY_Q_ech_ECS(value):
        Q_ech_ECS = c_double(value)
        lib.setY_Q_ech_ECS(byref(Q_ech_ECS))
    
    def setY_m_ECS(value):
        m_ECS = c_double(value)
        lib.setY_m_ECS(byref(m_ECS))
    
    def setY_Q_aller(value):
        Q_aller = c_double(value)
        lib.setY_Q_aller(byref(Q_aller))
    
    def setY_Q_retour(value):
        Q_retour = c_double(value)
        lib.setY_Q_retour(byref(Q_retour))
    
    def setY_T_ballon_out(value):
        T_ballon_out = c_double(value)
        lib.setY_T_ballon_out(byref(T_ballon_out))
    
    def setY_T_avg(value):
        T_avg = c_double(value)
        lib.setY_T_avg(byref(T_avg))
    
    def setY_T_mid(value):
        T_mid = c_double(value)
        lib.setY_T_mid(byref(T_mid))
    
    def setY_T_std(value):
        T_std = c_double(value)
        lib.setY_T_std(byref(T_std))
    
    def setY_T_half(value):
        T_half = c_double(value)
        lib.setY_T_half(byref(T_half))
    
    def setY_T_ECS_1(value):
        T_ECS_1 = c_double(value)
        lib.setY_T_ECS_1(byref(T_ECS_1))
    
    def setY_m_ECS_prim(value):
        m_ECS_prim = c_double(value)
        lib.setY_m_ECS_prim(byref(m_ECS_prim))
    
    def setY_m_sec(value):
        m_sec = c_double(value)
        lib.setY_m_sec(byref(m_sec))
    
    def setY_m_ch(value):
        m_ch = c_double(value)
        lib.setY_m_ch(byref(m_ch))
    
    def setY_Q_ECS_aller(value):
        Q_ECS_aller = c_double(value)
        lib.setY_Q_ECS_aller(byref(Q_ECS_aller))
    
    def setY_Q_ECS_retour(value):
        Q_ECS_retour = c_double(value)
        lib.setY_Q_ECS_retour(byref(Q_ECS_retour))
    
    def setY_eff_ech(value):
        eff_ech = c_double(value)
        lib.setY_eff_ech(byref(eff_ech))
    
    def setY_eff_ech_ECS(value):
        eff_ech_ECS = c_double(value)
        lib.setY_eff_ech_ECS(byref(eff_ech_ECS))
    
    def setY_m_2_ree(value):
        m_2_ree = c_double(value)
        lib.setY_m_2_ree(byref(m_2_ree))
    
    def setY_T_ECS_in(value):
        T_ECS_in = c_double(value)
        lib.setY_T_ECS_in(byref(T_ECS_in))
    
    def setY_T_in_emet(value):
        T_in_emet = c_double(value)
        lib.setY_T_in_emet(byref(T_in_emet))
    
    def setY(values):
        for values_, func in zip(values, [setY_T_sec_in, setY_T_out_ECS, setY_T_out, setY_T_ECS_sec_out, setY_T_ECS_sec_in, setY_T_ECS_prim_in, setY_T_ECS_prim_out, setY_T_ch_out, setY_T_ch_in, setY_T_prim_out, setY_T_sec_out, setY_T_out_emetteur, setY_T_ECS_n, setY_Q_ch, setY_Q_ech, setY_Q_ech_ECS, setY_m_ECS, setY_Q_aller, setY_Q_retour, setY_T_ballon_out, setY_T_avg, setY_T_mid, setY_T_std, setY_T_half, setY_T_ECS_1, setY_m_ECS_prim, setY_m_sec, setY_m_ch, setY_Q_ECS_aller, setY_Q_ECS_retour, setY_eff_ech, setY_eff_ech_ECS, setY_m_2_ree, setY_T_ECS_in, setY_T_in_emet]):
            func(values_)
    # -- P --
    
    def setP_Ballondestockage_D(value):
        Ballondestockage_D = c_double(value)
        lib.setP_Ballondestockage_D(byref(Ballondestockage_D))
    
    def setP_Chauffagealler_D(value):
        Chauffagealler_D = c_double(value)
        lib.setP_Chauffagealler_D(byref(Chauffagealler_D))
    
    def setP_Chauffageretour_D(value):
        Chauffageretour_D = c_double(value)
        lib.setP_Chauffageretour_D(byref(Chauffageretour_D))
    
    def setP_ECSaller_D(value):
        ECSaller_D = c_double(value)
        lib.setP_ECSaller_D(byref(ECSaller_D))
    
    def setP_ECSretour_D(value):
        ECSretour_D = c_double(value)
        lib.setP_ECSretour_D(byref(ECSretour_D))
    
    def setP_emetteurs_D(value):
        emetteurs_D = c_double(value)
        lib.setP_emetteurs_D(byref(emetteurs_D))
    
    def setP_Ballondestockage_H(value):
        Ballondestockage_H = c_double(value)
        lib.setP_Ballondestockage_H(byref(Ballondestockage_H))
    
    def setP_Chauffagealler_L(value):
        Chauffagealler_L = c_double(value)
        lib.setP_Chauffagealler_L(byref(Chauffagealler_L))
    
    def setP_Chauffageretour_L(value):
        Chauffageretour_L = c_double(value)
        lib.setP_Chauffageretour_L(byref(Chauffageretour_L))
    
    def setP_ECSaller_L(value):
        ECSaller_L = c_double(value)
        lib.setP_ECSaller_L(byref(ECSaller_L))
    
    def setP_ECSretour_L(value):
        ECSretour_L = c_double(value)
        lib.setP_ECSretour_L(byref(ECSretour_L))
    
    def setP_emetteurs_L(value):
        emetteurs_L = c_double(value)
        lib.setP_emetteurs_L(byref(emetteurs_L))
    
    def setP_Echangeurrseau_S(value):
        Echangeurrseau_S = c_double(value)
        lib.setP_Echangeurrseau_S(byref(Echangeurrseau_S))
    
    def setP_EchangeurECS_S(value):
        EchangeurECS_S = c_double(value)
        lib.setP_EchangeurECS_S(byref(EchangeurECS_S))
    
    def setP_emetteurs_T_air(value):
        emetteurs_T_air = c_double(value)
        lib.setP_emetteurs_T_air(byref(emetteurs_T_air))
    
    def setP_Ballondestockage_T_amb(value):
        Ballondestockage_T_amb = c_double(value)
        lib.setP_Ballondestockage_T_amb(byref(Ballondestockage_T_amb))
    
    def setP_Chauffagealler_T_local(value):
        Chauffagealler_T_local = c_double(value)
        lib.setP_Chauffagealler_T_local(byref(Chauffagealler_T_local))
    
    def setP_Chauffageretour_T_local(value):
        Chauffageretour_T_local = c_double(value)
        lib.setP_Chauffageretour_T_local(byref(Chauffageretour_T_local))
    
    def setP_ECSaller_T_local(value):
        ECSaller_T_local = c_double(value)
        lib.setP_ECSaller_T_local(byref(ECSaller_T_local))
    
    def setP_ECSretour_T_local(value):
        ECSretour_T_local = c_double(value)
        lib.setP_ECSretour_T_local(byref(ECSretour_T_local))
    
    def setP_Ballondestockage_U(value):
        Ballondestockage_U = c_double(value)
        lib.setP_Ballondestockage_U(byref(Ballondestockage_U))
    
    def setP_emetteurs_U(value):
        emetteurs_U = c_double(value)
        lib.setP_emetteurs_U(byref(emetteurs_U))
    
    def setP_Echangeurrseau_U(value):
        Echangeurrseau_U = c_double(value)
        lib.setP_Echangeurrseau_U(byref(Echangeurrseau_U))
    
    def setP_EchangeurECS_U(value):
        EchangeurECS_U = c_double(value)
        lib.setP_EchangeurECS_U(byref(EchangeurECS_U))
    
    def setP_Ballondestockage_V_min(value):
        Ballondestockage_V_min = c_double(value)
        lib.setP_Ballondestockage_V_min(byref(Ballondestockage_V_min))
    
    def setP_Ballondestockage_V_var(value):
        Ballondestockage_V_var = c_double(value)
        lib.setP_Ballondestockage_V_var(byref(Ballondestockage_V_var))
    
    def setP_Ballondestockage_eps(value):
        Ballondestockage_eps = c_double(value)
        lib.setP_Ballondestockage_eps(byref(Ballondestockage_eps))
    
    def setP_Chauffagealler_m_min(value):
        Chauffagealler_m_min = c_double(value)
        lib.setP_Chauffagealler_m_min(byref(Chauffagealler_m_min))
    
    def setP_Chauffageretour_m_min(value):
        Chauffageretour_m_min = c_double(value)
        lib.setP_Chauffageretour_m_min(byref(Chauffageretour_m_min))
    
    def setP_ECSaller_m_min(value):
        ECSaller_m_min = c_double(value)
        lib.setP_ECSaller_m_min(byref(ECSaller_m_min))
    
    def setP_ECSretour_m_min(value):
        ECSretour_m_min = c_double(value)
        lib.setP_ECSretour_m_min(byref(ECSretour_m_min))
    
    def setP_emetteurs_m_min(value):
        emetteurs_m_min = c_double(value)
        lib.setP_emetteurs_m_min(byref(emetteurs_m_min))
    
    def setP_Ballondestockage_n(value):
        Ballondestockage_n = c_double(value)
        lib.setP_Ballondestockage_n(byref(Ballondestockage_n))
    
    def setP_emetteurs_n_radiateurs(value):
        emetteurs_n_radiateurs = c_double(value)
        lib.setP_emetteurs_n_radiateurs(byref(emetteurs_n_radiateurs))
    
    def setP_emetteurs_n_tubes(value):
        emetteurs_n_tubes = c_double(value)
        lib.setP_emetteurs_n_tubes(byref(emetteurs_n_tubes))
    
    def setP_DelayRoot2_InitialCondition(value):
        DelayRoot2_InitialCondition = c_double(value)
        lib.setP_DelayRoot2_InitialCondition(byref(DelayRoot2_InitialCondition))
    
    def setP_DelayRoot3_InitialCondition(value):
        DelayRoot3_InitialCondition = c_double(value)
        lib.setP_DelayRoot3_InitialCondition(byref(DelayRoot3_InitialCondition))
    
    def setP_Constant1_Value(value):
        Constant1_Value = c_double(value)
        lib.setP_Constant1_Value(byref(Constant1_Value))
    
    def setP_Delay_InitialCondition(value):
        Delay_InitialCondition = c_double(value)
        lib.setP_Delay_InitialCondition(byref(Delay_InitialCondition))
    
    def setP_Delay_InitialCondition_l(value):
        Delay_InitialCondition_l = c_double(value)
        lib.setP_Delay_InitialCondition_l(byref(Delay_InitialCondition_l))
    
    def setP_Delay_InitialCondition_j(value):
        Delay_InitialCondition_j = c_double(value)
        lib.setP_Delay_InitialCondition_j(byref(Delay_InitialCondition_j))
    
    def setP_Delay1_InitialCondition(value):
        Delay1_InitialCondition = c_double(value)
        lib.setP_Delay1_InitialCondition(byref(Delay1_InitialCondition))
    
    def setP_Constant17_Value(value):
        Constant17_Value = c_double(value)
        lib.setP_Constant17_Value(byref(Constant17_Value))
    
    def setP_Delay_InitialCondition_o(value):
        Delay_InitialCondition_o = c_double(value)
        lib.setP_Delay_InitialCondition_o(byref(Delay_InitialCondition_o))
    
    def setP_Constant24_Value(value):
        Constant24_Value = c_double(value)
        lib.setP_Constant24_Value(byref(Constant24_Value))
    
    def setP_Delay2_InitialCondition(value):
        Delay2_InitialCondition = c_double(value)
        lib.setP_Delay2_InitialCondition(byref(Delay2_InitialCondition))
    
    def setP_Delay3_InitialCondition(value):
        Delay3_InitialCondition = c_double(value)
        lib.setP_Delay3_InitialCondition(byref(Delay3_InitialCondition))
    
    def setP_Delay5_InitialCondition(value):
        Delay5_InitialCondition = c_double(value)
        lib.setP_Delay5_InitialCondition(byref(Delay5_InitialCondition))
    
    def setP_Delay4_InitialCondition(value):
        Delay4_InitialCondition = c_double(value)
        lib.setP_Delay4_InitialCondition(byref(Delay4_InitialCondition))
    
    def setP_Delay_InitialCondition_o3(value):
        Delay_InitialCondition_o3 = c_double(value)
        lib.setP_Delay_InitialCondition_o3(byref(Delay_InitialCondition_o3))
    
    def setP_Delay_InitialCondition_k(value):
        Delay_InitialCondition_k = c_double(value)
        lib.setP_Delay_InitialCondition_k(byref(Delay_InitialCondition_k))
    
    def setP_Switch_Threshold(value):
        Switch_Threshold = c_double(value)
        lib.setP_Switch_Threshold(byref(Switch_Threshold))
    
    def setP_Delay_InitialCondition_o4(value):
        Delay_InitialCondition_o4 = c_double(value)
        lib.setP_Delay_InitialCondition_o4(byref(Delay_InitialCondition_o4))
    
    def setP_Constant25_Value(value):
        Constant25_Value = c_double(value)
        lib.setP_Constant25_Value(byref(Constant25_Value))
    
    def setP_Constant26_Value(value):
        Constant26_Value = c_double(value)
        lib.setP_Constant26_Value(byref(Constant26_Value))
    
    def setP_Gain_Gain(value):
        Gain_Gain = c_double(value)
        lib.setP_Gain_Gain(byref(Gain_Gain))
    
    def setP(values):
        for values_, func in zip(values, [setP_Ballondestockage_D, setP_Chauffagealler_D, setP_Chauffageretour_D, setP_ECSaller_D, setP_ECSretour_D, setP_emetteurs_D, setP_Ballondestockage_H, setP_Chauffagealler_L, setP_Chauffageretour_L, setP_ECSaller_L, setP_ECSretour_L, setP_emetteurs_L, setP_Echangeurrseau_S, setP_EchangeurECS_S, setP_emetteurs_T_air, setP_Ballondestockage_T_amb, setP_Chauffagealler_T_local, setP_Chauffageretour_T_local, setP_ECSaller_T_local, setP_ECSretour_T_local, setP_Ballondestockage_U, setP_emetteurs_U, setP_Echangeurrseau_U, setP_EchangeurECS_U, setP_Ballondestockage_V_min, setP_Ballondestockage_V_var, setP_Ballondestockage_eps, setP_Chauffagealler_m_min, setP_Chauffageretour_m_min, setP_ECSaller_m_min, setP_ECSretour_m_min, setP_emetteurs_m_min, setP_Ballondestockage_n, setP_emetteurs_n_radiateurs, setP_emetteurs_n_tubes, setP_DelayRoot2_InitialCondition, setP_DelayRoot3_InitialCondition, setP_Constant1_Value, setP_Delay_InitialCondition, setP_Delay_InitialCondition_l, setP_Delay_InitialCondition_j, setP_Delay1_InitialCondition, setP_Constant17_Value, setP_Delay_InitialCondition_o, setP_Constant24_Value, setP_Delay2_InitialCondition, setP_Delay3_InitialCondition, setP_Delay5_InitialCondition, setP_Delay4_InitialCondition, setP_Delay_InitialCondition_o3, setP_Delay_InitialCondition_k, setP_Switch_Threshold, setP_Delay_InitialCondition_o4, setP_Constant25_Value, setP_Constant26_Value, setP_Gain_Gain]):
            func(values_)
    
    
    # =======
    # MAPPERS
    # =======
    
    # -- U --
    
    mapper_U = {0: 'm_ch_dir', 1: 'm_ECS_sout', 2: 'm_ECS_stock', 3: 'm_ECS_sec', 4: 'm_ch_V3V', 5: 'm_prim', 6: 'T_prim_in', 7: 'T_edv', 8: 'm_ECS_dir', 9: 'm_ECS_V3V', 10: 'm_ECS_bouc'}
    # -- Y --
    
    mapper_Y = {0: 'T_sec_in', 1: 'T_out_ECS', 2: 'T_out', 3: 'T_ECS_sec_out', 4: 'T_ECS_sec_in', 5: 'T_ECS_prim_in', 6: 'T_ECS_prim_out', 7: 'T_ch_out', 8: 'T_ch_in', 9: 'T_prim_out', 10: 'T_sec_out', 11: 'T_out_emetteur', 12: 'T_ECS_n', 13: 'Q_ch', 14: 'Q_ech', 15: 'Q_ech_ECS', 16: 'm_ECS', 17: 'Q_aller', 18: 'Q_retour', 19: 'T_ballon_out', 20: 'T_avg', 21: 'T_mid', 22: 'T_std', 23: 'T_half', 24: 'T_ECS_1', 25: 'm_ECS_prim', 26: 'm_sec', 27: 'm_ch', 28: 'Q_ECS_aller', 29: 'Q_ECS_retour', 30: 'eff_ech', 31: 'eff_ech_ECS', 32: 'm_2_ree', 33: 'T_ECS_in', 34: 'T_in_emet'}
    # -- P --
    
    mapper_P = {0: 'Ballondestockage_D', 1: 'Chauffagealler_D', 2: 'Chauffageretour_D', 3: 'ECSaller_D', 4: 'ECSretour_D', 5: 'emetteurs_D', 6: 'Ballondestockage_H', 7: 'Chauffagealler_L', 8: 'Chauffageretour_L', 9: 'ECSaller_L', 10: 'ECSretour_L', 11: 'emetteurs_L', 12: 'Echangeurrseau_S', 13: 'EchangeurECS_S', 14: 'emetteurs_T_air', 15: 'Ballondestockage_T_amb', 16: 'Chauffagealler_T_local', 17: 'Chauffageretour_T_local', 18: 'ECSaller_T_local', 19: 'ECSretour_T_local', 20: 'Ballondestockage_U', 21: 'emetteurs_U', 22: 'Echangeurrseau_U', 23: 'EchangeurECS_U', 24: 'Ballondestockage_V_min', 25: 'Ballondestockage_V_var', 26: 'Ballondestockage_eps', 27: 'Chauffagealler_m_min', 28: 'Chauffageretour_m_min', 29: 'ECSaller_m_min', 30: 'ECSretour_m_min', 31: 'emetteurs_m_min', 32: 'Ballondestockage_n', 33: 'emetteurs_n_radiateurs', 34: 'emetteurs_n_tubes', 35: 'DelayRoot2_InitialCondition', 36: 'DelayRoot3_InitialCondition', 37: 'Constant1_Value', 38: 'Delay_InitialCondition', 39: 'Delay_InitialCondition_l', 40: 'Delay_InitialCondition_j', 41: 'Delay1_InitialCondition', 42: 'Constant17_Value', 43: 'Delay_InitialCondition_o', 44: 'Constant24_Value', 45: 'Delay2_InitialCondition', 46: 'Delay3_InitialCondition', 47: 'Delay5_InitialCondition', 48: 'Delay4_InitialCondition', 49: 'Delay_InitialCondition_o3', 50: 'Delay_InitialCondition_k', 51: 'Switch_Threshold', 52: 'Delay_InitialCondition_o4', 53: 'Constant25_Value', 54: 'Constant26_Value', 55: 'Gain_Gain'}
    

# liste des entrées, sorties et paramètres
if True:

    pass
    # 
    # ### ENTREES
    # 
    #       voir pilotage
    # 
    # - m_ch_dir
    # - m_ECS_sout
    # - m_ECS_stock
    # - m_ECS_sec
    # - m_ch_V3V
    # - m_prim
    # - T_prim_in
    # - T_edv
    # - m_ECS_dir
    # - m_ECS_V3V
    # - m_ECS_bouc
    # 
    # ### SORTIES
    # 
    #       voir pilotage
    # 
    # - T_sec_in
    # - T_out_ECS
    # - T_out
    # - T_ECS_sec_out
    # - T_ECS_sec_in
    # - T_ECS_prim_in
    # - T_ECS_prim_out
    # - T_ch_out
    # - T_ch_in
    # - T_prim_out
    # - T_sec_out
    # - T_out_emetteur
    # - T_ECS_n
    # - Q_ch
    # - Q_ech
    # - Q_ech_ECS
    # - m_ECS
    # - Q_aller
    # - Q_retour
    # - T_ballon_out
    # - T_avg
    # - T_mid
    # - T_std
    # - T_half
    # - T_ECS_1
    # - m_ECS_prim
    # - m_sec
    # - m_ch
    # - Q_ECS_aller
    # - Q_ECS_retour
    # - eff_ech
    # - eff_ech_ECS
    # - m_2_ree
    # - T_ECS_in
    # - T_in_emet
    # 
    # ### PARAMETRES
    # 
    #       obtenir la valeur actuelle: `getP_{nom_parametre}()`
    #       changer de valeur: `setP_{nom_parametre}(valeur)`
    # 
    # - Ballondestockage_D
    # - Chauffagealler_D
    # - Chauffageretour_D
    # - ECSaller_D
    # - ECSretour_D
    # - emetteurs_D
    # - Ballondestockage_H
    # - Chauffagealler_L
    # - Chauffageretour_L
    # - ECSaller_L
    # - ECSretour_L
    # - emetteurs_L
    # - Echangeurrseau_S
    # - EchangeurECS_S
    # - emetteurs_T_air
    # - Ballondestockage_T_amb
    # - Chauffagealler_T_local
    # - Chauffageretour_T_local
    # - ECSaller_T_local
    # - ECSretour_T_local
    # - Ballondestockage_U
    # - emetteurs_U
    # - Echangeurrseau_U
    # - EchangeurECS_U
    # - Ballondestockage_V_min
    # - Ballondestockage_V_var
    # - Ballondestockage_eps
    # - Chauffagealler_m_min
    # - Chauffageretour_m_min
    # - ECSaller_m_min
    # - ECSretour_m_min
    # - emetteurs_m_min
    # - Ballondestockage_n
    # - emetteurs_n_radiateurs
    # - emetteurs_n_tubes
    # - DelayRoot2_InitialCondition
    # - DelayRoot3_InitialCondition
    # - Constant1_Value
    # - Delay_InitialCondition
    # - Delay_InitialCondition_l
    # - Delay_InitialCondition_j
    # - Delay1_InitialCondition
    # - Constant17_Value
    # - Delay_InitialCondition_o
    # - Constant24_Value
    # - Delay2_InitialCondition
    # - Delay3_InitialCondition
    # - Delay5_InitialCondition
    # - Delay4_InitialCondition
    # - Delay_InitialCondition_o3
    # - Delay_InitialCondition_k
    # - Switch_Threshold
    # - Delay_InitialCondition_o4
    # - Constant25_Value
    # - Constant26_Value
    # - Gain_Gain

# fonction d'initialisation pour réglage du pas de temps: à appeler en tout début de script
if True:

    lib.initialize.argtypes = (POINTER(c_int), )
    def initialize(time_step: int):
        """Initialise le modèle physique avec le pas de temps `time_step`.
    
        Parameters
        ----------
        time_step : int, secondes
    
        Notes
        -----
        Le pas de temps ne doit pas être régler en dehors de cette fonction
        """
        stepSize0 = c_int(time_step)
        lib.initialize(byref(stepSize0))
    





















"""
A implémenter dans Simulink:
- composant stockage: modifier la précision d'affichage du message de correction débit trop grand
"""


def creer_loi_d_eau(*points: tuple[float, float]): # non important
    """Retourne une fonction par morceaux `func`
    
    Parameters
    -------
    points
        couples de coordonnées (x, y)

    Notes
    -----
    Pour un argument x < x_min, la fonction retourne y_min
    Pour un argument x > x_max, la fonction retourne y_max

    """
    xp = [p[0] for p in points]
    yp = [p[1] for p in points]
    assert np.all(np.diff(xp) > 0)
    points = sorted(points, key=lambda e: e[0])
    func = lambda x : np.interp(x, 
                                xp, 
                                yp) 
    return np.vectorize(func)





# données temporelles
time_step = 15               # ne pas modifier le pas de temps ici: appeler la fonction "initialize"

# sorties de références
P_ch_ref = pd.read_csv('donnees/batiment_1/NO.N.AB.01.Gen.ReEx.001.001_2014_2023.csv').iloc[:, 1].values # demande chauffage [kW/m2]
m_ECS_sout = pd.read_csv('donnees/batiment_1/NO.AB.ts60.cat4.occ34.persday40.res1.csv').iloc[:, 1].values  # soutirage ECS [kg/s] - pdt 60s
T_prim_out_ref = np.full(8760, 85)                                          # fixme: "70" donnée au Listic
T_ECS_in_ref = 60                                     
T_out_ECS_ref = 53
T_out_ECS_sec_ref = 65
m_ECS_bouc = 0.1

# conditions extérieures
df = pd.read_csv('donnees/batiment_1/TMY_Trondheim_2014_2023.csv')
T_ext =  df['temp_air'].values       # température extérieure [°C]
I_dir =  df['dni'].values     # irradiance directe     [W/m2]
I_diff = df['dhi'].values     # irradiance diffuse     [W/m2]
T_prim_in = creer_loi_d_eau((-10, 140), (15, 100))(T_ext)     # température primaire entrante (=aller) [°C]  
                                                              # sources: 
                                                              # - Guide des préconisations techniques du réseau de chauffage urbain de Grenoble-Alpes Métropole, page 7
                                                              # - Guide technique de conception de  sous-stations de réseaux de chaleur  et de secondaires associés optimisés, page 6

# T_prim_in est moyennée en glissant pour refléter l'incertitude liée au temps de propagation dans le réseau: moyennée sur 4h (mais ici pas de temps horaire)
T_prim_in = pd.Series(T_prim_in).rolling(4).mean().fillna(180).values
m_prim = np.full(8760, 0.1)                                   # débit primaire [kg/s]


def get_idx_largest_0_period(arr):
    """Determine the largest 0 period in a 1D array.

    Parameters
    ----------
    arr : np.ndarray, shape (n,)

    Returns
    -------
    (idx1, idx2)
        index of the first (resp last) element of the largest 0 period in `arr``
    """
    assert arr[0] > 0 and arr[-1] > 0  # aucune période nulle en début/fin d'array
    pos_idx = np.nonzero(arr)[0]
    large_gaps_idx_idx = np.argwhere(pos_idx[1:] - pos_idx[:-1]-1)[:, 0]
    m = 0
    m_idx = 0
    for idx in large_gaps_idx_idx:
        if pos_idx[idx+1] - pos_idx[idx] > m:
            m_idx = pos_idx[idx]
            m = pos_idx[idx+1] - pos_idx[idx]

    idx1, idx2 = m_idx + 1, m_idx + m -1
    return idx1, idx2



# passage des données au pas de temps demandé: interpolation linéaire
# optionnel: suppression de la période hors saison de chauffe et décalage temporel pour continuité
# optionnel : sélection d'une partie seulement des données avec `time_share`

time_share = 0.003
assert 0 < time_share <= 1
for idx, var_name in enumerate(['P_ch_ref', 'm_ECS_sout', 'T_prim_out_ref', 'T_ext', 'I_dir', 'I_diff', 'T_prim_in', 'm_prim']):
    var_ = globals()[var_name]
    
    ### rééchantillonage
    time_step_old = 365 * 24 * 3600 / len(var_)
    assert time_step_old - round(time_step_old) == 0, "Le pas de temps des données chargées n'est pas un nombre entier de secondes"
    print(f"Pas de temps actuel de {var_name} (longueur {len(var_)}): {time_step_old}")
    var_ = np.append(var_, var_[0])   # ajout de la première valeur pour avoir les valeurs de fin en interpolation
    index_ = pd.date_range('01/01/2019', freq=f'{time_step_old}s', periods=len(var_))
    var_ = pd.Series(var_, index=index_).resample(f'{time_step}s').interpolate()
    var_ = var_.iloc[:-1]
    print(f"Pas de temps modifié de {var_name} (longueur {len(var_)}): {365 * 24 * 3600 / len(var_)}\n")

    ### détection de la saison de chauffe
    if var_name == 'P_ch_ref':
        idx1, idx2 = get_idx_largest_0_period(var_.values)
        print(f"\n==> L'été commence le {var_.index[idx1].strftime('%d-%m')} \
                          et termine le {var_.index[idx2].strftime('%d-%m')} \
                          (pas de chauffage)\n")
    
    ### décalage temporel pour continuité
    # l'année démarre en début de saison de chauffage
    # l'année se termine en fin de saison de chauffage
    ###
    # var_ = pd.concat([var_[idx2+1:], var_[:idx1]])   


    ### sélection d'une partie seulement de la série temporelle (time_share): 
    ### les 1/10 des valeurs. Si série réordonnée, s'applique à la série réordonnée
    var_ = var_[:int(len(var_) * time_share)]

    ### enregistrement dans la variable de départ
    globals()[var_name] = var_.values

index_ = var_.index

# d'autres données temporelles
nbr_ts = len(index_)
t_end = nbr_ts * time_step             
time_range = np.arange(0, t_end, time_step)

# pondération multi objectifs: pour le moment, seulement mono objectif (demande chauffage)
coefs = (1, 0, 0, 0)


def calculer_erreur_totale(idx):
    P_ch_modele = sorties[idx]['Q_ch']
    T_prim_out_ = sorties[idx]['T_prim_out']
    T_ECS_in_ = sorties[idx]['T_ECS_in']
    T_out_ECS_ = sorties[idx]['T_out_ECS']
    erreur1 = ((P_ch_modele - P_ch_ref[idx]) / (P_ch_ref[idx]+1)) ** 2 # +1 sinon risque de div par 0
    erreur2 = ((T_prim_out_ - T_prim_out_ref[idx]) / T_prim_out_ref[idx]) ** 2 
    erreur3 = ((T_ECS_in_ - T_ECS_in_ref) / T_ECS_in_ref) ** 2 
    erreur4 = ((T_out_ECS_ - T_out_ECS_ref) / T_out_ECS_ref) ** 2 
    erreur  = coefs[0] * erreur1 + coefs[1] * erreur2 + coefs[2] * erreur3 + coefs[3] * erreur4
    erreurs[idx]['erreur1'] = erreur1
    erreurs[idx]['erreur2'] = erreur2
    erreurs[idx]['erreur3'] = erreur3       # fixme: non tracée en postprocessing
    erreurs[idx]['erreur4'] = erreur4
    erreurs[idx]['erreur'] =  erreur

def executer_modele_phy(idx):
    # conversion du dictionnaire en liste, avec vérification que toutes les entrées sont présentes
    entrees_ = [0] * len(mapper_U)
    for k in range(len(mapper_U)):
        value = entrees[idx].get(mapper_U[k])
        if value is None:
            raise ValueError(f"Pas de temps {idx}: valeur d'entrée {mapper_U[k]} manquante.")
        else:
            entrees_[k] = value
    # envoi entrées vers C 
    setU(entrees_)
    # exécution modèle physique
    lib.parallele_ECS_Stock_aval_step() 
    # récupération sorties              
    sorties_ = getY()
    # conversion sorties en dictionnaire et assignation dans conteneur global
    if sorties[idx]:  # dict non vide
        raise IndexError(f"Pas de temps {idx}: une sortie existe déjà.")
    sorties[idx] = {mapper_Y[k]: sorties_[k] for k in range(len(mapper_Y))}


def traiter_consignes(idx):
    executer_modele_phy(idx)
    calculer_erreur_totale(idx)


def proposer_pilotage(idx, pilote):
    pilote.piloter(idx)


class PilotageLoiDEauTemperature:
    """Débit circuit chauffage qui suit une consigne et température sortie V3V loi d'eau (multi segments) par rapport à température extérieure.
    Le pilotage est réalisé en modifiant:
     - m_prim: asservissement pour respect consigne T_sec_out_ref
     - la proportion de m_sec (et m_V3V): respecter la loi d'eau T_ch_in_ref.
     - m_sec et m_V3V (à ratio constant): respecter de la consigne m_ch_ref. A tout moment, le débit chauffage m_ch vérifie m_sec + m_V3V. 

     
     Si m_ch variable, le délai de propagation est variable.
     Le délai de propagation induit un décalage entre puissance consigne et puissance satisfaite car le pilotage n'est pas anticipateur (demande reflétée par la loi d'eau, exploitée en t pour produire les consignes en t)
    """


    def __init__(self):
        T_air = getP_emetteurs_T_air()   # température de l'air intérieur émetteurs chauffage: 
                                          # si l'eau entre à cette température aucune demande n'est satisfaite, équivalent à un débit nul
        self.T_ch_in_ref = creer_loi_d_eau((-15, 110), (-5, 85), (15, 30), (16, T_air))(T_ext)  # consigne de température de sortie de V3V, i.e. circuit chauffage
        
        # [°C]  température de l'eau sortie sec SST:  dépend de T_ch_in_ref
        self.T_sec_out_ref = np.full(len(T_prim_in), 112)
                                       # np.minimum(np.maximum(self.T_ch_in_ref+5,                                 # fixme: à corriger dans "chauffage_seul"
                                       #            np.full(len(T_prim_in), T_ECS_in_ref+10)),
                                       #            T_prim_in +5)

        self.m_ch_ref = creer_loi_d_eau((-15, 0.175), (15, 0.175), (16, 0))(T_ext)                        # [kg/s] débit circuit chauffage 
        self.T_ECS_in_ref = 60                                     
        self.T_out_ECS_ref = 53
        self.T_out_ECS_sec_ref = 65
        self.m_ECS_bouc = 0.1
        self.dm = 0.0025         # [kg/s] variation élémentaire de débit pour correction 
        self.T_ch_in = 0        # [°C] température de sortie V3V du pdt précédent 
        # self.debit_primaire = {}
        # self.decharge_stockage = {}
        # self.etat = {}

    def piloter(self, idx):
        m_ECS_prim_ = 0.15
        m_ECS_stock_max_charge    = 0.1   
        entrees[idx]['m_ECS_bouc'] = 0.1 
        entrees[idx]['T_prim_in'] = T_prim_in[idx]
        entrees[idx]['m_ECS_sout'] =  0.2 # m_sout_ref[idx] # 0.1 * (np.sin(idx/(len(self.T_ch_in_ref)) * 2 * np.pi) + 1) / 2 + 0.05 # 0.25
        # print(entrees[idx]['m_ECS_sout'])
        entrees[idx]['T_edv'] = 10
        entrees[idx]['m_ECS'] = 0.38        # fixme: temporaire
        

        
        if idx == 0:                            # pas d'historique de mesure des températures, donc supposition de débits 
            entrees[idx]['m_ch_dir'] = self.m_ch_ref[idx] / 2
            entrees[idx]['m_ch_V3V'] = self.m_ch_ref[idx] / 2
            entrees[idx]['m_ECS_stock'] = m_ECS_stock_max_charge
            entrees[idx]['m_ECS_dir'] = m_ECS_prim_ / 2 + entrees[idx]['m_ECS_stock']
            entrees[idx]['m_ECS_V3V'] = m_ECS_prim_ / 2
            entrees[idx]['m_prim'] = 2
            entrees[idx]['m_ECS_sec'] = 0.01
            
            entrees[idx]['m_ECS_sout'] = m_ECS_sout[idx]  
            self.statut_charge = 'oui'
            self.statut_decharge = 'non'
            # self.decharge_stockage[idx] = True
            # self.debit_primaire[idx] = False



        else:
            #### chauffage
            if self.m_ch_ref[idx] == 0:    # absence de demande supposée, débit nul
                entrees[idx]['m_ch_dir'] = 0
                entrees[idx]['m_ch_V3V'] = 0

            elif self.m_ch_ref[idx-1] == 0: # en t, demande existante supposée, mais pas en t-1,
                                                         # donc les mesures du pdt précédent (t-1) sont erronées pour prévoir ce pdt (t). 
                                                         # On suppose un fort débit m_V3V car
                                                         # ces conditions correspondent souvent à l'été où la demande est faible
                entrees[idx]['m_ch_dir'] = self.m_ch_ref[idx] * 0.2
                entrees[idx]['m_ch_V3V'] = self.m_ch_ref[idx] * 0.8

            else:                     

                # réglage départ chauffage               # cas général
                self.T_ch_in = (entrees[idx-1]['m_ch_dir']*sorties[idx-1]['T_sec_out'] + entrees[idx-1]['m_ch_V3V']*sorties[idx-1]['T_ch_out'])/self.m_ch_ref[idx-1] 
                if self.T_ch_in < self.T_ch_in_ref[idx]:
                    dm_ = min(entrees[idx-1]['m_ch_V3V'], self.dm)       # on ne peut soustraire plus de débit que ce qui est disponible
                    entrees[idx]['m_ch_dir'] = entrees[idx-1]['m_ch_dir'] + dm_       # température trop faible, un peu plus d'eau chaude
                    entrees[idx]['m_ch_V3V'] = entrees[idx-1]['m_ch_V3V'] - dm_     
                else:
                    dm_ = min(entrees[idx-1]['m_ch_dir'], self.dm)
                    entrees[idx]['m_ch_dir'] = entrees[idx-1]['m_ch_dir'] - dm_        # température trop élevée, un peu moins d'eau chaude
                    entrees[idx]['m_ch_V3V'] = entrees[idx-1]['m_ch_V3V'] + dm_

            # mise à l'échelle des débits chauffage
            if (entrees[idx]['m_ch_dir']+entrees[idx]['m_ch_V3V']) != 0:
                ratio_m_ch = self.m_ch_ref[idx] / (entrees[idx]['m_ch_dir']+entrees[idx]['m_ch_V3V'])      # mise à l'échelle des débits pour respect consigne
                entrees[idx]['m_ch_dir'] *= ratio_m_ch
                entrees[idx]['m_ch_V3V'] *= ratio_m_ch
        
           
            # ----- Pilotage ECS (stockage en aval de l'échangeur ECS) -----
            # Initialisation de dm

            # 1. Répartition du flux entre stockage (m_ECS_stock) et secondaire (m_ECS_sec)
            if sorties[idx-1]['T_ECS_in'] < self.T_ECS_in_ref:
            # Besoin d'une eau plus chaude en entrée d'échangeur ECS
                if sorties[idx-1]['T_ballon_out'] > 60:
                        # Vérifier que le ballon était en mode décharge
                    if entrees[idx-1]['m_ECS_stock'] < 0:
                            # On peut prélever au ballon
                        dm_stoc = min(abs(entrees[idx-1]['m_ECS_stock']), self.dm)
                        entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock'] - dm_stoc
                        entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec'] - dm_stoc
                    else:
                            # Impossible de décharger, garder les valeurs précédentes
                        entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock']
                        entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec']
                # Ouvrir plus vers le ballon de stockage
                    dm_stoc = min(abs(entrees[idx-1]['m_ECS_stock']), self.dm)
                    entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock'] - dm_stoc
                    entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec'] - dm_stoc
                else:
                # Priorité boucle secondaire si possible
                    if entrees[idx-1]['m_ECS_sec'] > 0:
                        dm_sec = min(abs(entrees[idx-1]['m_ECS_sec']), self.dm)
                        entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock'] - dm_sec
                        entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec'] + dm_sec
                    else:
                    # Boucle secondaire indisponible
                        entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock']
                        entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec']
            else:
            # Bonne température, on garde la répartition précédente
                entrees[idx]['m_ECS_stock'] = entrees[idx-1]['m_ECS_stock']
                entrees[idx]['m_ECS_sec'] = entrees[idx-1]['m_ECS_sec']

        # 2. Gestion de la charge/décharge du ballon
            if entrees[idx-1]['m_ECS_stock']> 0:
            # Stockage en charge
                if sorties[idx-1]['T_ballon_out'] > 65:
                    # Passe en décharge
                    entrees[idx]['m_ECS_stock'] = -min(abs(entrees[idx]['m_ECS_stock']), 0.1)
                    entrees[idx]['m_ECS_sec'] = entrees[idx]['m_ECS_sout'] + entrees[idx]['m_ECS_bouc'] - abs(entrees[idx]['m_ECS_stock'])
                else:
                    # Continue la charge
                    entrees[idx]['m_ECS_stock'] = 0.1
                    entrees[idx]['m_ECS_sec'] = entrees[idx]['m_ECS_sout'] + entrees[idx]['m_ECS_bouc'] + abs(entrees[idx]['m_ECS_stock'])  
            else:
            # Stockage en décharge
                if sorties[idx-1]['T_ballon_out'] < 55:
                    # Passe en charge
                    entrees[idx]['m_ECS_stock'] = 0.1
                    entrees[idx]['m_ECS_sec'] = entrees[idx]['m_ECS_sout'] + entrees[idx]['m_ECS_bouc'] + abs(entrees[idx]['m_ECS_stock'])
                else:
                    # Continue la décharge
                    entrees[idx]['m_ECS_stock'] = -min(abs(entrees[idx]['m_ECS_stock']), 0.1)
                    entrees[idx]['m_ECS_sec'] = entrees[idx]['m_ECS_sout'] + entrees[idx]['m_ECS_bouc'] - abs(entrees[idx]['m_ECS_stock'])
        # 3. Réglage sortie de l'échangeur ECS
            if sorties[idx-1]['T_ECS_sec_out'] < self.T_out_ECS_sec_ref:
                # Augmenter m_ECS_prim (ouvrir davantage la vanne vers m_ECS_dir)
                dm_dir = min(abs(entrees[idx-1]['m_ECS_dir']),self.dm)
                entrees[idx]['m_ECS_dir'] = entrees[idx-1]['m_ECS_dir'] + dm_dir
                entrees[idx]['m_ECS_V3V'] = entrees[idx-1]['m_ECS_V3V']- dm_dir
            else:
                # Ouvrir davantage la vanne vers m_ECS_V3V
                #dm_V3V = min(entrees[idx-1]['m_ECS_V3V'], self.dm)
                entrees[idx]['m_ECS_dir'] = entrees[idx-1]['m_ECS_dir']
                entrees[idx]['m_ECS_V3V'] = entrees[idx-1]['m_ECS_V3V'] 

        # 4. Réglage du primaire pour le chauffage seul 
            if (entrees[idx]['m_ch_dir'] + entrees[idx]['m_ECS_dir']) != 0:
                if sorties[idx-1]['T_sec_out'] < self.T_sec_out_ref[idx]:
                    dm_ = self.dm
                    entrees[idx]['m_prim'] = entrees[idx-1]['m_prim'] + dm_
                else:
                    dm_ = min(entrees[idx-1]['m_prim'], self.dm)
                    entrees[idx]['m_prim'] = entrees[idx-1]['m_prim'] - dm_
            else:
                entrees[idx]['m_prim'] = 0

     

def piloter():

    initialize(time_step) 

    pilote = PilotageLoiDEauTemperature()

    for idx in tqdm.tqdm(range(nbr_ts)): #, miniters=5000):
        entrees[idx] = {}
        sorties[idx] = {}
        erreurs[idx] = {}
        proposer_pilotage(idx, pilote)
        traiter_consignes(idx)   

def posttraiter(plot=True):
    global entrees, sorties, erreurs
    entrees = pd.DataFrame.from_dict(entrees, orient='index')
    entrees.index = index_
    entrees = entrees.sort_index()          # pour que le 1er janvier soit bien au début
    entrees.columns = [f'{c} (in)' for c in entrees.columns]


    sorties = pd.DataFrame.from_dict(sorties, orient='index')
    l1 = f"P_chauffage_ref (coef={coefs[0]})"
    sorties[l1] = P_ch_ref
    l2 = f"T_prim_out_ref (coef={coefs[1]})"
    sorties[l2] = T_prim_out_ref
    l3 = f"T_ECS_in_ref (coef={coefs[2]})"
    sorties[l3] = T_ECS_in_ref
    l4 = f"T_out_ECS_ref (coef={coefs[3]})"
    sorties[l4] = T_out_ECS_ref
    sorties.index = index_
    sorties = sorties.sort_index()          # pour que le 1er janvier soit bien au début
    erreurs = pd.DataFrame.from_dict(erreurs, orient='index')
    erreurs.index = index_
    erreurs = erreurs.sort_index()          # pour que le 1er janvier soit bien au début

    print(f'Reference - demande       : L_moyen: {erreurs.loc[:,'erreur1'].mean():.3f}')
    print(f'Reference - température   : L_moyen: {erreurs.loc[:,'erreur2'].mean():.3f}')
    print(f'Reference - température endtree ECS  : L_moyen: {erreurs.loc[:,'erreur3'].mean():.3f}')
    print(f'Reference - température de sortie ECS  : L_moyen: {erreurs.loc[:,'erreur4'].mean():.3f}')
    # print(sorties.iloc[1000].T)
    # print(entrees.iloc[1000].T)

    # Nettoyage si besoin
 
    slice_ = slice(None)

    # sorties
    
    if plot:
        # 1. Erreurs (conservé identique)
        sr = erreurs.iloc[slice_, 2]
        ax = sr.plot()
        ax.set_ylim((0, 1))
        ax = pd.Series(sr.sort_values().values, index=sr.index).plot(title='Erreur de pilotage', color='red', secondary_y=True, figsize=(16, 9))
        ax.set_yscale('log')
        fig = ax.get_figure()
        fig.canvas.manager.set_window_title('Erreurs')
        fig.tight_layout()

        # 2. Chauffage - Version améliorée
        fig_ch, axes = plt.subplots(3, 1, figsize=(16, 12), sharex=True)
        
        # a. Températures
        sorties.iloc[slice_][['T_ch_out', 'T_ch_in']].plot(ax=axes[0], color=['r', 'b'], title='Températures circuit chauffage')
        sorties.iloc[slice_][['T_out_emetteur', 'T_in_emet']].plot(ax=axes[1], color=['g', 'm'], title='Températures émetteurs')
        
        # b. Puissances (Q_ch, Q_aller, Q_retour)
        sorties.iloc[slice_][['Q_ch', 'Q_aller', 'Q_retour']].plot(
            ax=axes[2], 
            color=['k', 'c', 'y'],
            title='Puissances chauffage'
        )
        axes[2].set_ylabel('W')
        
        fig_ch.canvas.manager.set_window_title('Chauffage')
        fig_ch.tight_layout()

        # 3. Bouclage ECS - Version corrigée
        fig_bouc, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True)
        
        # Températures
        sorties.iloc[slice_][['T_ECS_in', 'T_out_ECS']].plot(ax=ax1, style=['-r', '--b'], title='Températures bouclage ECS')
        
        # Débits combinés
        sorties.iloc[slice_]['m_ECS'].plot(ax=ax2, color='blue', label='m_ECS (sortie)')
        entrees.iloc[slice_][['m_ECS_bouc (in)', 'm_ECS_sout (in)']].plot(
            ax=ax2, 
            style=[':g', '-.r'], 
            title='Débits bouclage ECS'
        )
        ax2.legend()
        
        fig_bouc.canvas.manager.set_window_title('Bouclage ECS')
        fig_bouc.tight_layout()

        # 4. Échangeur SST (conservé identique)
        fig_sst, axes = plt.subplots(3, 1, figsize=(16, 9), sharex=True)
        # Températures
        entrees.iloc[slice_][['T_prim_in (in)']].plot(ax=axes[0], color='r')
        sorties.iloc[slice_][['T_prim_out', 'T_sec_in', 'T_sec_out']].plot(
            ax=axes[0], 
            color=['m', 'g', 'b'],
            title='Températures échangeur SST'
        )
        # Débits
        entrees.iloc[slice_][['m_prim (in)']].plot(ax=axes[1], color='k')
        sorties.iloc[slice_][['m_sec']].plot(ax=axes[1], color='c', title='Débits')
        # Puissance
        sorties.iloc[slice_][['Q_ech']].plot(ax=axes[2], color='r', title='Puissance échangée')
        
        fig_sst.canvas.manager.set_window_title('Echangeur SST')
        fig_sst.tight_layout()

        # 5. Échangeur ECS (conservé identique)
        fig_ecs, axes = plt.subplots(3, 1, figsize=(16, 9), sharex=True)
        # Températures
        sorties.iloc[slice_][['T_ECS_prim_in', 'T_ECS_prim_out']].plot(
            ax=axes[0], 
            color=['r', 'm'],
            title='Températures primaire'
        )
        sorties.iloc[slice_][['T_ECS_sec_in', 'T_ECS_in']].plot(
            ax=axes[0], 
            color=['g', 'b'],
            title='Températures secondaire'
        )
        # Débits
        entrees.iloc[slice_][['m_ECS_V3V (in)']].plot(ax=axes[1], color='r')
        sorties.iloc[slice_][['m_ECS_prim', 'm_ECS']].plot(
            ax=axes[1], 
            color=['m', 'g'],
            title='Débits'
        )
        # Puissance
        sorties.iloc[slice_][['Q_ech_ECS']].plot(ax=axes[2], color='k', title='Puissance échangée')
        
        fig_ecs.canvas.manager.set_window_title('Echangeur ECS')
        fig_ecs.tight_layout()

        # 6. Stockage ECS (conservé identique)
        fig_stock, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 9), sharex=True)
        sorties.iloc[slice_][['T_ECS_1', 'T_ECS_n', 'T_ballon_out']].plot(
            ax=ax1, 
            color=['r', 'g', 'b'],
            title='Températures ballon'
        )
        entrees.iloc[slice_][['m_ECS_stock (in)', 'm_ECS_dir (in)']].plot(
            ax=ax2,
            color=['m', 'c'],
            title='Débits stockage'
        )
        
        fig_stock.canvas.manager.set_window_title('Stockage ECS')
        fig_stock.tight_layout()

        plt.show()

if __name__ == '__main__':
    entrees = {}
    sorties = {}
    erreurs = {}
    piloter()   
    posttraiter(True)
    # Nettoyage si besoin
    
## tentative de calage de modele (pilotage temperature loi d'eau, débit fixe)
# recherche du débit qui minimise l'erreur annuelle

# def fun(m):
#     m = m[0]
#     global entrees, sorties, erreurs
#     entrees = {}
#     sorties = {}
#     erreurs = {}
#     PilotageLoiDEauTemperature.m_ch_ref = m
#     piloter()   
#     posttraiter(plot=False)

#     print(PilotageLoiDEauTemperature.m_ch_ref)
#     erreur1 = erreurs.loc[:,'erreur1'].mean()
#     return erreur1


# from scipy.optimize import minimize
# res = minimize(fun, [0.12], bounds=[(0.1, 1)], method='Powell')
# print(res)



## tentative de calage de modele (pilotage temperature loi d'eau, débit fixe)
# connaissant une puissance et la température de l'eau correspondante, on cherche le débit à faire circuler pour satisfaire cette puissance
# fait intervenir le DT_lm et une recherche de zero/minimum

# idx = 350000
# T_ch_in = PilotageLoiDEauTemperature.T_ch_in_loi_deau[idx]
# T_air = PilotageLoiDEauTemperature.T_air
# Cp = 4180
# S = getP_Radiateurs_S()
# Kg = getP_Radiateurs_U()
# P_ = P_ch[idx]
# print(P_, T_ch_in)
# def fun(m):
#     T_ch_out = max(T_ch_in - P_ /(m*Cp), T_air+0.1)
#     return (P_ - S * Kg * ((T_ch_in-T_air)-(T_ch_out-T_air)) / np.log((T_ch_in-T_air)/(T_ch_out-T_air)))**2

# from scipy.optimize import minimize
# res = minimize(fun, 0.3, bounds=[(0, None)])
# print(res)




















####
#  brouillon: ne pas utiliser
###
# figure: erreur (signée) en fonction de la température extérieure
# attention: étendue y modifiée
# l1 = f"P_chauffage_ref (coef=1)"
# P_ch = "P_chauffage"
# sr=((sorties[l1]-sorties[P_ch])/(sorties[l1]+1))
# sr = np.sign(sr) * (sr**2)
# sr = pd.Series(sr, index=index_, name="erreur (signe)").sort_index()
# T_ext_=pd.Series(T_ext, index=index_, name="T_ext").sort_index()
# df = pd.concat([sorties, erreurs, T_ext_, sr], axis=1)
# df.plot.scatter(x="T_ext", y="erreur (signe)", ylim=(-2,2), s=1, title='reference-observe')
