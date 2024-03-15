# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 18:09:24 2020

@author: Sabrina
"""
import numpy as np

def uncertanity_one_line(line, line_uc, line_factor, line_factor_uc):
    line = line/10**30
    line_uc = line_uc/10**30
    uncertanity = np.sqrt((line_uc*line_factor)**2+(line*line_factor_uc)**2)
    return uncertanity*10**30


def uncertanity_two_lines(line1, line1_uc, line1_factor, line1_factor_uc, line2,
                          line2_uc, line2_factor, line2_factor_uc):
    line1 = line1/10**30
    line1_uc = line1_uc/10**30
    line2 = line2/10**30
    line2_uc = line2_uc/10**30
    uncertanity = np.sqrt((line1_uc*line1_factor)**2+(line1*line1_factor_uc)**2+
                          (line2_uc*line2_factor)**2+(line2*line2_factor_uc)**2)
    return uncertanity*10**30


def uncertanity_three_lines(line1, line1_uc, line1_factor, line1_factor_uc,
                            line2, line2_uc, line2_factor, line2_factor_uc,
                            line3, line3_uc, line3_factor, line3_factor_uc):
    line1 = np.array(line1/10**30)
    line1_uc = np.array(line1_uc/10**30)
    line2 = np.array(line2/10**30)
    line2_uc = np.array(line2_uc/10**30)
    line3 = np.array(line3/10**30)
    line3_uc = np.array(line3_uc/10**30)
    uncertanity = np.sqrt((line1_uc*line1_factor)**2+(line1*line1_factor_uc)**2+
                          (line2_uc*line2_factor)**2+(line2*line2_factor_uc)**2+
                          (line3_uc*line3_factor)**2+(line3*line3_factor_uc)**2)
    return uncertanity*10**30


def uncertanity_four_lines(line1, line1_uc, line1_factor, line1_factor_uc,
                           line2, line2_uc, line2_factor, line2_factor_uc,
                           line3, line3_uc, line3_factor, line3_factor_uc,
                           line4, line4_uc, line4_factor, line4_factor_uc):
    line1 = line1/10**30
    line1_uc = line1_uc/10**30
    line2 = line2/10**30
    line2_uc = line2_uc/10**30
    line3 = line3/10**30
    line3_uc = line3_uc/10**30
    line4 = line4/10**30
    line4_uc = line4_uc/10**30
    print(line1, line1_uc, line2, line2_uc, line3, line3_uc, line4, line4_uc)
    uncertanity = np.sqrt((line1_uc*line1_factor)**2
                          +(line1*line1_factor_uc)**2
                          +
                          (line2_uc*line2_factor)**2
                          +(line2*line2_factor_uc)**2
                          +
                          (line3_uc*line3_factor)**2
                          +(line3*line3_factor_uc)**2
                          +
                          (line4_uc*line4_factor)**2
                          +(line4*line4_factor_uc)**2
                          )
    return uncertanity*10**30


def uncertanity_five_lines(line1, line1_uc, line1_factor, line1_factor_uc,
                           line2, line2_uc, line2_factor, line2_factor_uc,
                           line3, line3_uc, line3_factor, line3_factor_uc,
                           line4, line4_uc, line4_factor, line4_factor_uc,
                           line5, line5_uc, line5_factor, line5_factor_uc):
    line1 = line1/10**30
    line1_uc = line1_uc/10**30
    line2 = line2/10**30
    line2_uc = line2_uc/10**30
    line3 = line3/10**30
    line3_uc = line3_uc/10**30
    line4 = line4/10**30
    line4_uc = line4_uc/10**30
    line5 = line5/10**30
    line5_uc = line5_uc/10**30
    uncertanity = np.sqrt((line1_uc*line1_factor)**2+(line1*line1_factor_uc)**2+
                          (line2_uc*line2_factor)**2+(line2*line2_factor_uc)**2+
                          (line3_uc*line3_factor)**2+(line3*line3_factor_uc)**2+
                          (line4_uc*line4_factor)**2+(line4*line4_factor_uc)**2+
                          (line5_uc*line5_factor)**2+(line5*line5_factor_uc)**2)
    return uncertanity*10**30


def calc_sigtir(i24=np.array([False]), i24_uc=np.array([False]),
                i70=np.array([False]), i70_uc=np.array([False]),
                i100=np.array([False]), i100_uc=np.array([False]),
                i160=np.array([False]), i160_uc=np.array([False]),
                i250=np.array([False]), i250_uc=np.array([False]),):

    """
    This is the Python version of "calc_sigir.pro" which
    is part of the "cpropstoo/physical" package
    translated to python by Johannes Puschnig, 2019

    NOTE: compared to the idl version, some flux combinations were added
    though still some combinations missing.

    Implements Table 3 of Galametz+ 13
    
    I've implemented the surface density conversions, the luminosity
    conversions are very similar, though not identical.
    """
    
    # CHECK WHICH BANDS WE HAVE
    have24 = i24.all() > 0 or False
    have70 = i70.all() > 0 or False
    have100 = i100.all() > 0 or False
    have160 = i160.all() > 0 or False
    have250 = i250.all() > 0 or False
    
    have24_uc = i24_uc.all() > 0 or False
    have70_uc = i70_uc.all() > 0 or False
    have100_uc = i100_uc.all() > 0 or False
    have160_uc = i160_uc.all() > 0 or False
    have250_uc = i250_uc.all() > 0 or False
    # print(have24, have70, have100, have160, have250)
    # print('24', i24, '70', i70, '100', i100, '169', i160, '250', i250)
    line_names = np.array([i24, i70, i100, i160, i250])
    for line in line_names:
        line[line <= 0.] = np.nan
    # CONSTANTS
    c = 2.99792458*1e10
    pc = 3.0857*1e18
    nu24 = c/(24.0*1e-4)
    nu70 = c/(70.0*1e-4)
    nu100 = c/(100.0*1e-4)
    nu160 = c/(160.0*1e-4)
    nu250 = c/(250.0*1e-4)
    
    # MJY/SR -> W/KPC^2
    fac24 = nu24*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac70 = nu70*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac100 = nu100*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac160 = nu160*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac250 = nu250*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    # print('facs', fac24, fac70, fac100, fac100, fac160, fac250)
    
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    # MONOCHROMATIC CONVERSIONS
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    
    # TBD
    
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    # HYBRID CONVERSIONS
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    # 24+70
    if have24 and have70 and not have100 and not have160 and not have250:
        s_tir = \
            (3.925)*i24*fac24 + \
            (1.551)*i70*fac70
        s_tir_uc = \
            uncertanity_two_lines(i24*fac24, i24_uc*fac24, 3.925, 0.284,
                                  i70*fac70, i70_uc*fac70, 1.551, 0.059)
        return s_tir, s_tir_uc
    
    # 24 + 100
    elif have24 and have100 and not have70 and not have160 and not have250:
        s_tir = \
            (2.421)*i24*fac24 + \
            (1.410)*i100*fac100
        s_tir_uc = \
            uncertanity_two_lines(i24*fac24, i24_uc*fac24, 2.421, 0.086,
                                  i100*fac100, i100_uc*fac100, 1.410, 0.014)
        return s_tir, s_tir_uc
    
    # 24 + 160
    elif have24 and have160 and not have70 and not have100 and not have250:
        s_tir = \
            (3.854)*i24*fac24 + \
            (1.373)*i160*fac160
        s_tir_uc = \
            uncertanity_two_lines(i24*fac24, i24_uc*fac24, 3.854, 0.088,
                                  i160*fac160, i160_uc*fac160, 1.373, 0.015)
        return s_tir, s_tir_uc
    
    # 24 + 250
    elif have24 and have250 and not have70 and not have100 and not have160:
        s_tir = \
            (5.179)*i24*fac24 + \
            (3.196)*i250*fac250
        s_tir_uc = \
            uncertanity_two_lines(i24*fac24, i24_uc*fac24, 5.179, 0.132,
                                  i250*fac250, i250_uc*fac250, 3.196, 0.059)
        return s_tir, s_tir_uc
    
    # 70+100
    elif have70 and have100 and not have24 and not have160 and not have250:
        s_tir = \
        (0.458)*i70*fac70 + \
        (1.444)*i100*fac100
        s_tir_uc = \
            uncertanity_two_lines(i70*fac70, i70_uc*fac70, 0.458, 0.034,
                                  i100*fac100, i100_uc*fac100, 1.444, 0.023)
        return s_tir, s_tir_uc

    # 70+160
    elif have70 and have160 and not have24 and not have100 and not have250:
        s_tir = \
                (0.999)*i70*fac70 + \
                (1.226)*i160*fac160
        s_tir_uc = \
            uncertanity_two_lines(i70*fac70, i70_uc*fac70, 0.999, 0.023,
                                  i160*fac160, i160_uc*fac160, 1.226, 0.017)
        return s_tir, s_tir_uc

    # 70+250
    elif have70 and have250 and not have24 and not have100 and not have160:
        s_tir = \
                (1.306)*i70*fac70 + \
                (2.752)*i250*fac250
        s_tir_uc = \
            uncertanity_two_lines(i70*fac70, i70_uc*fac70, 1.306, 0.021,
                                  i250*fac250, i250_uc*fac250, 2.752, 0.044)
        return s_tir, s_tir_uc

    # 100+160
    elif have100 and have160 and not have24 and not have70 and not have250:
        s_tir = \
                (1.238)*i100*fac100 + \
                (0.620)*i160*fac160
        s_tir_uc = \
            uncertanity_two_lines(i100*fac100, i100_uc*fac100, 1.239, 0.025,
                                  i160*fac160, i160_uc*fac160, 0.620, 0.028)
        return s_tir, s_tir_uc
    
    # 100+250
    elif have100 and have250 and not have24 and not have70 and not have160:
        s_tir = \
                (1.403)*i100*fac100 + \
                (1.242)*i250*fac250
        s_tir_uc = \
            uncertanity_two_lines(i100*fac100, i100_uc*fac100, 1.403, 0.016,
                                  i250*fac250, i250_uc*fac250, 1.242, 0.048)
        return s_tir, s_tir_uc
    
    # 160+250
    elif have160 and have250 and not have24 and not have70 and not have100:
        s_tir = \
                (2.342)*i160*fac160 + \
                (-0.944)*i250*fac250
        s_tir_uc = \
            uncertanity_two_lines(i160*fac160, i160_uc*fac160, 2.342, 0.040,
                                  i250*fac250, i250_uc*fac250, -0.944, 0.111)
        return s_tir, s_tir_uc
    
    # 24+70+100
    elif have24 and have70 and have100 and not have160 and not have250:
        s_tir = \
                (2.162)*i24*fac24 + \
                (0.185)*i70*fac70 + \
                (1.319)*i100*fac100
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 2.162, 0.113,
                                    i70*fac70, i70_uc*fac70, 0.185, 0.035,
                                    i100*fac100, i100_uc*fac100, 1.319, 0.016)
        return s_tir, s_tir_uc
    
    # 24+70+160
    elif have24 and have70 and have160 and not have100 and not have250:
        s_tir = \
                (2.126)*i24*fac24 + \
                (0.670)*i70*fac70 + \
                (1.134)*i160*fac160
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 2.126, 0.093,
                                    i70*fac70, i70_uc*fac70, 0.670, 0.028,
                                    i160*fac160, i160_uc*fac160, 1.134, 0.010)
        return s_tir, s_tir_uc

    # 24+70+250
    elif have24 and have70 and have250 and not have100 and not have160:
        s_tir = \
            (2.317)*i24*fac24 + \
            (0.922)*i70*fac70 + \
            (2.525)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 2.317, 0.114,
                                    i70*fac70, i70_uc*fac70, 0.922, 0.028,
                                    i250*fac250, i250_uc*fac250, 2.525, 0.030)
        return s_tir, s_tir_uc
    
    # 24+100+160
    elif have24 and have100 and have160 and not have70 and not have250:
        s_tir = \
            (2.708)*i24*fac24 + \
            (0.734)*i100*fac100 + \
            (0.739)*i160*fac160
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 2.708, 0.071,
                                    i100*fac100, i100_uc*fac100, 0.734, 0.022,
                                    i160*fac160, i160_uc*fac160, 0.739, 0.018)
        return s_tir, s_tir_uc
    
    # 24+100+250
    elif have24 and have100 and have250 and not have70 and not have160:
        s_tir = \
            (2.561)*i24*fac24 + \
            (0.933)*i100*fac100 + \
            (1.338)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 2.561, 0.072,
                                    i100*fac100, i100_uc*fac100, 0.993, 0.017,
                                    i250*fac250, i250_uc*fac250, 1.338, 0.032)
        return s_tir, s_tir_uc
    
    # 24+160+250
    elif have24 and have160 and have250 and not have70 and not have100:
        s_tir= \
            (3.826)*i24*fac24 + \
            (1.460)*i160*fac160 + \
            (-0.237)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i24*fac24, i24_uc*fac24, 3.826, 0.089,
                                    i160*fac160, i160_uc*fac160, 1.460, 0.032,
                                    i250*fac250, i250_uc*fac250, -0.237, 0.067)
        return s_tir, s_tir_uc
    
    # 70+100+160
    elif have70 and have100 and have160 and not have24 and not have250:
        s_tir = \
            (0.789)*i70*fac70 + \
            (0.387)*i100*fac100 + \
            (0.960)*i160*fac160
        s_tir_uc = \
            uncertanity_three_lines(i70*fac70, i70_uc*fac70, 0.789, 0.032,
                                    i100*fac100, i100_uc*fac100, 0.387, 0.029,
                                    i160*fac160, i160_uc*fac160, 0.960, 0.020)
        return s_tir, s_tir_uc
    
    # 70+100+250
    elif have70 and have100 and have250 and not have24 and not have160:
        s_tir = \
            (0.688)*i70*fac70 + \
            (0.795)*i100*fac100 + \
            (1.634)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i70*fac70, i70_uc*fac70, 0.688, 0.028,
                                    i100*fac100, i100_uc*fac100, 0.795, 0.022,
                                    i250*fac250, i250_uc*fac250, 1.634, 0.043)
        return s_tir, s_tir_uc
    
    # 70+160+250
    elif have70 and have160 and have250 and not have24 and not have100:
        s_tir = \
            (1.018)*i70*fac70 + \
            (1.068)*i160*fac160 + \
            (0.402)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i70*fac70, i70_uc*fac70, 1.018, 0.021,
                                    i160*fac160, i160_uc*fac160, 1.068, 0.035,
                                    i250*fac250, i250_uc*fac250, 0.402, 0.097)
        return s_tir, s_tir_uc
    
    # 100+160+250
    elif have100 and have160 and have250 and not have24 and not have70:
        s_tir = \
            (1.363)*i100*fac100 + \
            (0.097)*i160*fac160 + \
            (1.090)*i250*fac250
        s_tir_uc = \
            uncertanity_three_lines(i100*fac100, i100_uc*fac100, 0.795, 0.022,
                                    i160*fac160, i160_uc*fac160, 1.068, 0.035,
                                    i250*fac250, i250_uc*fac250, 0.402, 0.097)
        return s_tir, s_tir_uc
    
    # 24+70+100+160
    elif have24 and have70 and have100 and have160 and not have250:
        s_tir = \
            (2.051)*i24*fac24 + \
            (0.521)*i70*fac70 + \
            (0.294)*i100*fac100 + \
            (0.934)*i160*fac160
        s_tir_uc = \
            uncertanity_four_lines(i24*fac24, i24_uc*fac24, 2.051, 0.089,
                                   i70*fac70, i70_uc*fac70, 0.521, 0.030,
                                   i100*fac100, i100_uc*fac100, 0.294, 0.019,
                                   i160*fac160, i160_uc*fac160, 0.934, 0.014)
        return s_tir, s_tir_uc
    
    # 24+70+100+250
    elif have24 and have70 and have100 and have250 and not have160:
        s_tir = \
            (1.983)*i24*fac24 + \
            (0.427)*i70*fac70 + \
            (0.708)*i100*fac160 + \
            (1.561)*i250*fac250
        s_tir_uc = \
            uncertanity_four_lines(i24*fac24, i24_uc*fac24, 1.983, 0.084,
                                   i70*fac70, i70_uc*fac70, 0.427, 0.026,
                                   i100*fac100, i100_uc*fac100, 0.708, 0.017,
                                   i250*fac250, i250_uc*fac250, 1.561, 0.030)
        return s_tir, s_tir_uc
 
    # 24+70+160+250
    elif have24 and have70 and have160 and have250 and not have100:
        s_tir = \
            (2.119)*i24*fac24 + \
            (0.688)*i70*fac70 + \
            (0.995)*i160*fac160 + \
            (0.354)*i250*fac250
        s_tir_uc = \
            uncertanity_four_lines(i24*fac24, i24_uc*fac24, 2.119, 0.090,
                                   i70*fac70, i70_uc*fac70, 0.688, 0.025,
                                   i160*fac160, i160_uc*fac160, 0.995, 0.027,
                                   i250*fac250, i250_uc*fac250, 0.354, 0.068)
        return s_tir, s_tir_uc
    
    # 24+100+160+250
    elif have24 and have100 and have160 and have250 and not have70:
        s_tir = \
            (2.643)*i24*fac24 + \
            (0.836)*i100*fac100 + \
            (0.357)*i160*fac160 + \
            (0.791)*i250*fac250
        s_tir_uc = \
            uncertanity_four_lines(i24*fac24, i24_uc*fac24, 2.643, 0.069,
                                   i100*fac100, i100_uc*fac100, 0.836, 0.024,
                                   i160*fac160, i160_uc*fac160, 0.357, 0.042,
                                   i250*fac250, i250_uc*fac250, 0.791, 0.072)
        return s_tir, s_tir_uc
    
    # 70+100+160+250
    elif have70 and have100 and have160 and have250 and not have24:
        s_tir = \
            (0.767)*i70*fac70 + \
            (0.503)*i100*fac100 + \
            (0.558)*i160*fac160 + \
            (0.814)*i250*fac250
        s_tir_uc = \
            uncertanity_four_lines(i70*fac70, i70_uc*fac70, 0.767, 0.032,
                                   i100*fac100, i100_uc*fac100, 0.503, 0.038,
                                   i160*fac160, i160_uc*fac160, 0.558, 0.059,
                                   i250*fac250, i250_uc*fac250, 0.814, 0.111)
        return s_tir, s_tir_uc
    
    # 24+70+100+160+250
    elif have24 and have70 and have100 and have160 and have250:
        s_tir = \
            (2.013)*i24*fac24 + \
            (0.508)*i70*fac70 + \
            (0.393)*i100*fac100 + \
            (0.599)*i160*fac160 + \
            (0.680)*i250*fac250
        s_tir_uc = \
            uncertanity_five_lines(i24*fac24, i24_uc*fac24, 2.013, 0.081,
                                   i70*fac70, i70_uc*fac70, 0.508, 0.029,
                                   i100*fac100, i100_uc*fac100, 0.393, 0.025,
                                   i160*fac160, i160_uc*fac160, 0.599, 0.042,
                                   i250*fac250, i250_uc*fac250, 0.680, 0.078,)
        # print('all', s_tir)
        return s_tir, s_tir_uc
    
    else:
        print("CALC_SIGTIR Warning, SIGTIR could not be calculated.")
        print(i24, i70, i100, i160, i250)
        return np.nan



def calc_sigtir_without_uc(i24=np.array([False]), i70=np.array([False]),
                i100=np.array([False]), i160=np.array([False]),
                i250=np.array([False])):

    """
    This is the Python version of "calc_sigir.pro" which
    is part of the "cpropstoo/physical" package
    translated to python by Johannes Puschnig, 2019

    NOTE: compared to the idl version, some flux combinations were added
    though still some combinations missing.

    Implements Table 3 of Galametz+ 13
    
    I've implemented the surface density conversions, the luminosity
    conversions are very similar, though not identical.
    """
    
    # CHECK WHICH BANDS WE HAVE
    have24 = i24.all() > 0 or False
    have70 = i70.all() > 0 or False
    have100 = i100.all() > 0 or False
    have160 = i160.all() > 0 or False
    have250 = i250.all() > 0 or False
    # print(have24, have70, have100, have160, have250)
    # print('24', i24, '70', i70, '100', i100, '169', i160, '250', i250)
    
    # CONSTANTS
    c = 2.99792458*1e10
    pc = 3.0857*1e18
    nu24 = c/(24.0*1e-4)
    nu70 = c/(70.0*1e-4)
    nu100 = c/(100.0*1e-4)
    nu160 = c/(160.0*1e-4)
    nu250 = c/(250.0*1e-4)
    
    # MJY/SR -> W/KPC^2
    fac24 = nu24*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac70 = nu70*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac100 = nu100*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac160 = nu160*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    fac250 = nu250*1e-17*1e-7*4*np.pi*(pc*1e3)**2
    # print('facs', fac24, fac70, fac100, fac100, fac160, fac250)
    
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    # MONOCHROMATIC CONVERSIONS
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    
    # TBD
    
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    # HYBRID CONVERSIONS
    # &%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%&%
    
    # 24+70
    if have24 and have70 and not have100 and not have160 and not have250:
        s_tir = \
        (3.925)*i24*fac24 + \
        (1.551)*i70*fac70
        return s_tir
    
    # 24 + 100
    elif have24 and have100 and not have70 and not have160 and not have250:
        s_tir = \
        (2.421)*i24*fac24 + \
        (1.410)*i100*fac100
        return s_tir
    
    # 24 + 160
    elif have24 and have160 and not have70 and not have100 and not have250:
        s_tir = \
        (3.854)*i24*fac24 + \
        (1.373)*i160*fac160
        return s_tir
    
    # 24 + 250
    elif have24 and have250 and not have70 and not have100 and not have160:
        s_tir = \
        (5.179)*i24*fac24 + \
        (3.196)*i250*fac250
        return s_tir
    
    # 70+100
    elif have70 and have100 and not have24 and not have160 and not have250:
        s_tir = \
        (0.458)*i70*fac70 + \
        (1.444)*i100*fac100
        return s_tir

    # 70+160
    elif have70 and have160 and not have24 and not have100 and not have250:
        s_tir = \
                (0.999)*i70*fac70 + \
                (1.226)*i160*fac160
        return s_tir

    # 70+250
    elif have70 and have250 and not have24 and not have100 and not have160:
        s_tir = \
                (1.306)*i70*fac70 + \
                (2.752)*i250*fac250
        return s_tir

    # 100+160
    elif have100 and have160 and not have24 and not have70 and not have250:
        s_tir = \
                (1.238)*i100*fac100 + \
                (0.620)*i160*fac160
        return s_tir
    
    # 100+250
    elif have100 and have250 and not have24 and not have70 and not have160:
        s_tir = \
                (1.403)*i100*fac100 + \
                (1.242)*i250*fac250
        return s_tir
    
    # 160+250
    elif have160 and have250 and not have24 and not have70 and not have100:
        s_tir = \
                (2.342)*i160*fac160 + \
                (-0.944)*i250*fac250
        return s_tir
    
    # 24+70+100
    elif have24 and have70 and have100 and not have160 and not have250:
        s_tir = \
                (2.162)*i24*fac24 + \
                (0.185)*i70*fac70 + \
                (1.319)*i100*fac100
        return s_tir
    
    # 24+70+160
    elif have24 and have70 and have160 and not have100 and not have250:
        s_tir = \
                (2.126)*i24*fac24 + \
                (0.670)*i70*fac70 + \
                (1.134)*i160*fac160
        return s_tir

    # 24+70+250
    elif have24 and have70 and have250 and not have100 and not have160:
        s_tir = \
        (2.317)*i24*fac24 + \
        (0.922)*i70*fac70 + \
        (2.525)*i250*fac250
        return s_tir
    
    # 24+100+160
    elif have24 and have100 and have160 and not have70 and not have250:
        s_tir = \
        (2.708)*i24*fac24 + \
        (0.734)*i100*fac100 + \
        (0.739)*i160*fac160
        return s_tir
    
    # 24+100+250
    elif have24 and have100 and have250 and not have70 and not have160:
        s_tir = \
        (2.561)*i24*fac24 + \
        (0.933)*i100*fac100 + \
        (1.338)*i250*fac250
        return s_tir
    
    # 24+160+250
    elif have24 and have160 and have250 and not have70 and not have100:
        (3.826)*i24*fac24 + \
        (1.460)*i160*fac160 + \
        (-0.237)*i250*fac250
        return s_tir
    
    # 70+100+160
    elif have70 and have100 and have160 and not have24 and not have250:
        s_tir = \
        (0.789)*i70*fac70 + \
        (0.387)*i100*fac100 + \
        (0.960)*i160*fac160
        return s_tir
    
    # 70+100+250
    elif have70 and have100 and have250 and not have24 and not have160:
        s_tir = \
        (0.688)*i70*fac70 + \
        (0.795)*i100*fac100 + \
        (1.634)*i250*fac250
        return
    
    # 70+160+250
    elif have70 and have160 and have250 and not have24 and not have100:
        s_tir = \
        (1.018)*i70*fac70 + \
        (1.068)*i160*fac160 + \
        (0.402)*i250*fac250
        return s_tir
    
    # 100+160+250
    elif have100 and have160 and have250 and not have24 and not have70:
        s_tir = \
        (1.363)*i100*fac100 + \
        (0.097)*i160*fac160 + \
        (1.090)*i250*fac250
        return s_tir
    
    # 24+70+100+160
    elif have24 and have70 and have100 and have160 and not have250:
        s_tir = \
        (2.051)*i24*fac24 + \
        (0.521)*i70*fac70 + \
        (0.294)*i100*fac100 + \
        (0.934)*i160*fac160
        return s_tir
    
    # 24+70+100+250
    elif have24 and have70 and have100 and have250 and not have160:
        s_tir = \
        (1.983)*i24*fac24 + \
        (0.427)*i70*fac70 + \
        (0.708)*i100*fac160 + \
        (1.561)*i250*fac250
        return s_tir
 
    # 24+70+160+250
    elif have24 and have70 and have160 and have250 and not have100:
        s_tir = \
        (2.119)*i24*fac24 + \
        (0.688)*i70*fac70 + \
        (0.995)*i160*fac160 + \
        (0.354)*i250*fac250
        return s_tir
    
    # 24+100+160+250
    elif have24 and have100 and have160 and have250 and not have70:
        s_tir = \
        (2.643)*i24*fac24 + \
        (0.836)*i100*fac100 + \
        (0.357)*i160*fac160 + \
        (0.791)*i250*fac250
        return s_tir
    
    # 70+100+160+250
    elif have70 and have100 and have160 and have250 and not have24:
        s_tir = \
        (0.767)*i70*fac70 + \
        (0.503)*i100*fac100 + \
        (0.558)*i160*fac160 + \
        (0.814)*i250*fac250
        return s_tir
    
    # 24+70+100+160+250
    elif have24 and have70 and have100 and have160 and have250:
        s_tir = \
        (2.013)*i24*fac24 + \
        (0.508)*i70*fac70 + \
        (0.393)*i100*fac100 + \
        (0.599)*i160*fac160 + \
        (0.680)*i250*fac250
        # print('all', s_tir)
        return s_tir
    
    else:
        print("CALC_SIGTIR Warning, SIGTIR could not be calculated.")
        print(i24, i70, i100, i160, i250)
        return np.nan

