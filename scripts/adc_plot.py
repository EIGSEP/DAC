import numpy as np
import matplotlib.pyplot as plt
import glob
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter



parser = ArgumentParser(description = 'plot', formatter_class = ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', dest = 'file_number_', type = str, help = 'File ending for data')

parser.add_argument('--p1', action = 'store_true', help = 'Display plot: max amplitudes')
parser.add_argument('--p2', action = 'store_true', help = 'Display plot: adc1')
parser.add_argument('--p3', action = 'store_true', help = 'Display plot: adc2')
parser.add_argument('--p4', action = 'store_true', help = 'Display plot: ave')
parser.add_argument('--p5', action = 'store_true', help = 'Display plots: ave and amp1')
parser.add_argument('--p6', action = 'store_true', help = 'Display plots: stack')
args = parser.parse_args()
file_number = args.file_number_


directory = '/home/dominiv/simulink/dac/adc_data/'
ending = file_number

#amp1_list = sorted(glob.glob(directory + 'max_amp1_/*'))
#amp2_list = sorted(glob.glob(directory + 'max_amp2_/*'))
#adc1_list = sorted(glob.glob(directory + 'adc1_/*'))
#adc2_list = sorted(glob.glob(directory + 'adc2_/*'))
#x_list = sorted(glob.glob(directory + 'counts_/*'))
#ave_list = sorted(glob.glob(directory + 'ave_/*'))
#



#amp1_array = []
#amp2_array = []
#adc1_array = []
#adc2_array = []
#x_array = []
#ave_array = []
#
#
#
#
#
#for i in amp1_list:
#    data = np.load(i)
#    amp1_array.append(data)
#
#for i in amp2_list:
#    data = np.load(i)
#    amp2_array.append(data)
#
#for i in adc1_list:
#    data = np.load(i)
#    adc1_array.append(data)
#
#for i in adc2_list:
#    data = np.load(i)
#    adc2_array.append(data)
#
#for i in x_list:
#    data = np.load(i)
#    x_array.append(data)
#
#for i in ave_list:
#    data = np.load(i)
#    ave_array.append(data)
#
#
#amp1 = np.concatenate(amp1_array, axis = 0)
#amp2 = np.concatenate(amp2_array, axis = 0)
#adc1 = np.concatenate(adc1_array, axis = 0)
#adc2 = np.concatenate(adc2_array, axis = 0)
#x = np.concatenate(x_array, axis = 0)
#ave = np.concatenate(ave_array, axis = 0)
#
##ave = ave
#
#print('amp1 shape:', amp1.shape)
#print('amp2 shape:', amp2.shape)
#print('adc1 shape:', adc1.shape)
#print('adc2 shape:', adc2.shape)
#print('count shape:', x.shape)
#print('ave shape:', ave.shape)
#
if args.p1:
    amp1_list = sorted(glob.glob(directory + 'max_amp1' + str(ending) +'/*'))
    amp1_array = []
    for i in amp1_list:
        data = np.load(i)
        amp1_array.append(data)
    amp1 = np.concatenate(amp1_array, axis = 0)

    amp2_list = sorted(glob.glob(directory + 'max_amp2'+str(ending)+'/*'))
    amp2_array = []
    for i in amp2_list:
        data = np.load(i)
        amp2_array.append(data)
    amp2 = np.concatenate(amp2_array, axis = 0)
    print('amp1 shape:', amp1.shape)
    print('amp2 shape:', amp2.shape)

    fig, ax = plt.subplots(2,1, sharex=True, sharey=False, figsize=(10,6))
    ax[0].plot(amp1, label = 'max amp1')
    ax[0].set_title('amp1')

    ax[1].plot(amp2, label = 'max amp2')
    ax[1].set_title('amp2')
    plt.tight_layout()
    plt.legend()
    plt.show()
    #plt.figure()
    #plt.plot(amp2, label = 'Amp2')
    #plt.legend()
    #plt.ylabel('Max amplitudes')
    #plt.xlabel('Counts')
    #plt.show()

if args.p2:
    adc1_list = sorted(glob.glob(directory + 'adc1'+str(ending)+'/*'))
    adc1_array = []
    for i in adc1_list:
        data = np.load(i)
        adc1_array.append(data)
    adc1 = np.concatenate(adc1_array, axis = 0)

    adc2_list = sorted(glob.glob(directory + 'adc2'+str(ending)+'/*'))
    adc2_array = []
    for i in adc2_list:
        data = np.load(i)
        adc2_array.append(data)
    adc2 = np.concatenate(adc2_array, axis = 0)
    print('adc1 shape:', adc1.shape)
    print('adc2 shape:', adc2.shape)
    fig, ax = plt.subplots(2,1, sharex=True, sharey=False, figsize=(10,6))
    ax[0].plot(adc1[0], label = 'input')
    ax[0].set_title('ADC1')

    ax[1].plot(adc2[0], label = 'input')
    ax[1].set_title('ADC2')
    plt.tight_layout()
    plt.legend()
    plt.show()
    #plt.figure()
    #plt.plot(adc1[0], label = 'adc1 data')
    #plt.legend()
    #plt.ylabel('Amplitudes')
    #plt.xlabel('Counts')
    #plt.show()


if args.p3:
    plt.figure()
    plt.plot(adc2[0], label = 'adc2 data')
    plt.legend()
    plt.ylabel('Amplitudes')
    plt.xlabel('Counts')
    plt.show()

if args.p4:
    plt.figure()
    plt.plot(ave[0], label = 'ave data')
    plt.legend()
    plt.ylabel('Average Temp')
    plt.xlabel('Counts')
    plt.show()

if args.p5:
    ave_list = sorted(glob.glob(directory + 'ave' + str(ending) +'/*'))
    ave_array = []
    for i in ave_list:
        data = np.load(i)
        ave_array.append(data)
    ave = np.concatenate(ave_array, axis = 0)
    #ave = ave/13.076923076923105# - 9.6

    amp2_list = sorted(glob.glob(directory + 'max_amp2' + str(ending) +'/*'))
    amp2_array = []
    for i in amp2_list:
        data = np.load(i)
        amp2_array.append(data)
    amp2 = np.concatenate(amp2_array, axis = 0)
    print('ave shape:', ave.shape)
    print('amp2 shape:', amp2.shape)
#
    #from scipy.interpolate import interp1d
    #n_bits = 8
    #V_ref = 5
    #R_fixed = 10000
    #V_in = 4.1
    #
    ## Resistance (Ohms) and corresponding temperature (Celsius) from datasheet
    ##resistance_values = np.array([277.2, 51.82, 31.77, 19.68, 10, 2.472, .6744, .2258, .1027, .0619]) * 1e3 # Example values
    #resistance_values = np.loadtxt('/home/dominiv/simulink/dac/scripts/celsius_data.txt')[:,0] * 1e3 # Example values
    ##temperature_values = np.array([-40, -10, 0, 10, 25, 60, 100, 140, 175, 200])  # Corresponding temperatures
    #temperature_values = np.loadtxt('/home/dominiv/simulink/dac/scripts/celsius_data.txt')[:,1]  # Corresponding temperatures
    #print((resistance_values.shape), len(temperature_values.shape))
    ## Create interpolation function
    #resistance_to_temp = interp1d(resistance_values, temperature_values, kind='linear', fill_value="extrapolate")
    #
    #def bits_to_temperature_table(bits):
    #    # Step 1: Calculate V_out
    #    V_out = (bits / (2**n_bits - 1)) * V_ref
    #
    #    # Step 2: Calculate R_thermistor
    #    R_thermistor = R_fixed * ((V_in / V_out) - 1)
    #
    #    # Step 3: Get temperature using interpolation
    #    T_celsius = resistance_to_temp(R_thermistor)
    #
    #    return T_celsius
    #
    ## Example usage:
    #adc_bits = 638
    #temperature = bits_to_temperature_table(adc_bits)
    #temp = bits_to_temperature_table(ave[8:])
    ##print(f"Temperature: {temperature:.2f} °C")
#    
    
    
    
    


    fig, ax = plt.subplots(2,1, sharex=True, sharey=False, figsize=(10,6))
    #ax[0].plot(ave[8:], label = 'average temp')
    ax[0].plot(ave[8:], label = 'average temp')
    ax[0].set_ylabel('Celsius')
    ax[0].set_title('Temperature')

    ax[1].plot(amp2[8:], label = 'max value of dac')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('max amp bit')
    ax[1].set_title('DAC')
    plt.tight_layout()
    plt.legend()
    plt.show()




if args.p6:
    ave_list = sorted(glob.glob(directory + 'ave' + str(ending) +'_on'+'/*'))
    ave_array = []
    for i in ave_list:
        data = np.load(i)
        ave_array.append(data)
    aven = np.concatenate(ave_array, axis = 0)
    #ave = ave/13.076923076923105# - 9.6

    amp2_list = sorted(glob.glob(directory + 'max_amp2' + str(ending) +'_on'+'/*'))
    amp2_array = []
    for i in amp2_list:
        data = np.load(i)
        amp2_array.append(data)
    amp2n = np.concatenate(amp2_array, axis = 0)
    print('ave shape:', aven.shape)
    print('amp2 shape:', amp2n.shape)
    
    ave_list = sorted(glob.glob(directory + 'ave' + str(ending)+ '_off'+'/*'))
    ave_array = []
    for i in ave_list:
        data = np.load(i)
        ave_array.append(data)
    avef = np.concatenate(ave_array, axis = 0)
    #ave = ave/13.076923076923105# - 9.6

    amp2_list = sorted(glob.glob(directory + 'max_amp2' + str(ending) +'_off'+'/*'))
    amp2_array = []
    for i in amp2_list:
        data = np.load(i)
        amp2_array.append(data)
    amp2f = np.concatenate(amp2_array, axis = 0)
#
    #from scipy.interpolate import interp1d
    #n_bits = 8
    #V_ref = 5
    #R_fixed = 10000
    #V_in = 4.1
    #
    ## Resistance (Ohms) and corresponding temperature (Celsius) from datasheet
    ##resistance_values = np.array([277.2, 51.82, 31.77, 19.68, 10, 2.472, .6744, .2258, .1027, .0619]) * 1e3 # Example values
    #resistance_values = np.loadtxt('/home/dominiv/simulink/dac/scripts/celsius_data.txt')[:,0] * 1e3 # Example values
    ##temperature_values = np.array([-40, -10, 0, 10, 25, 60, 100, 140, 175, 200])  # Corresponding temperatures
    #temperature_values = np.loadtxt('/home/dominiv/simulink/dac/scripts/celsius_data.txt')[:,1]  # Corresponding temperatures
    #print((resistance_values.shape), len(temperature_values.shape))
    ## Create interpolation function
    #resistance_to_temp = interp1d(resistance_values, temperature_values, kind='linear', fill_value="extrapolate")
    #
    #def bits_to_temperature_table(bits):
    #    # Step 1: Calculate V_out
    #    V_out = (bits / (2**n_bits - 1)) * V_ref
    #
    #    # Step 2: Calculate R_thermistor
    #    R_thermistor = R_fixed * ((V_in / V_out) - 1)
    #
    #    # Step 3: Get temperature using interpolation
    #    T_celsius = resistance_to_temp(R_thermistor)
    #
    #    return T_celsius
    #
    ## Example usage:
    #adc_bits = 638
    #temperature = bits_to_temperature_table(adc_bits)
    #temp = bits_to_temperature_table(ave[8:])
    ##print(f"Temperature: {temperature:.2f} °C")
#    
    
    
    ave = np.concatenate((aven, avef))#*0.02635658914728682
    amp2 = np.concatenate((amp2n, amp2f))
    print(ave.shape, amp2.shape)


    fig, ax = plt.subplots(2,1, sharex=True, sharey=False, figsize=(10,6))
    #ax[0].plot(ave[8:], label = 'average temp')
    ax[0].plot(ave, label = 'average temp')
    ax[0].set_ylabel('Celsius')
    ax[0].set_title('Temperature')

    ax[1].plot(amp2, label = 'max value of dac')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('max amp bit')
    ax[1].set_title('DAC')
    plt.tight_layout()
    plt.legend()
    plt.show()
