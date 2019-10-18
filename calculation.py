import math

def mass_calc():
    file1 = open('Mv_stars_ini.txt')
    file2 = open('MvDistLimits.txt')
    if file2:
        limits = {}
        for line in file2:
            if not (line[0] == '#' or line[0]=='\n'):
                data = line.split()
                limits[data[0]] = data[1]
    print(limits)
    if file1 :
        list = []
        dict = {}
        for line in file1 :
            mv = float(line)
            if mv<10 :
                log_mass = 0.477 - (0.135*mv) + (0.01228*pow(mv,2)) - (0.0006734*pow(mv,3))
                mass = pow(10,log_mass)
                for x in range(0,16):
                    if(math.floor(mv) == x):
                        dict[x] = dict.get(x,0) + 1
                        break
                    
                list.append(mass)

            else :
                log_mass = pow(10,-3)*(0.3+(1.87*mv)+(7.614*pow(mv,2))-(1.698*pow(mv,3))+(0.06096*pow(mv,4)))
                mass = pow(10,log_mass)
                for x in range(0,16):
                    if(math.floor(mv) == x):
                        dict[x] = dict.get(x,0) + 1
                        break
                list.append(mass)
            # dict[mv]=mass
        print(dict)
        # return dict
              
                
    else :
        print('file not open! Error..!')
        return False

mass_calc()
