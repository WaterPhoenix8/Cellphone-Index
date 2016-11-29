globe = ['0817', '0905', '0906', '0915', '0916', '0917', '09173', '09175', '09176', '09178', '09253', '09256', '09257', '0926', '0927', '0935', '0936', '0937', '0945', '0975', '0976', '0977', '0978', '0979', '0994', '0995', '0996', '0997']
smart = ['0813', '0900', '0907', '0908', '0909', '0910', '0911', '0912', '0913', '0914', '0918', '0919', '0920', '0921', '0928', '0929', '0930', '0938', '0939', '0946', '0947', '0948', '0949', '0950', '0951', '0981', '0989', '0998', '0999'] #, '0956']
sun = ['0922', '0923', '0924', '0925', '09255', '09258', '0931', '0932', '0933', '0934', '0942', '0943', '0944']
extelcom = ['0973', '0974']

prefix = input('Enter Cellphone Prefix No. Please: ')

#if prefix == '0925':
    #print('The number is both GLOBE and SUN!')
if prefix in globe:
    print('The number is a GLOBE number!')
elif prefix in smart:
    print('The number is a SMART number!')
elif prefix in sun:
    print('The number is a SUN number!')
elif prefix in extelcom:
    print('The number is an EXTELCOM number!')
else:
    print('NOT a PREFIX NUMBER as of November 2016!')
