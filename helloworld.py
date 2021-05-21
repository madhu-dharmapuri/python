import math
'''
path = "hdfs://nameservice1/client1/marketrisk/rfds/u-h/data_refresh_scratch"

print(path)
n = path.count("/")
print (n)
path_table = "hdfs://nameservice1/client1/marketrisk/rfds/u-h/data_refresh_scratch/pv_manifest/cobdate=10-OCT-2020/runtype=hsv_ 1d_ car/valcontextid=hsv-      10d_     vvar/dsloadid=12234/grainid=qwqwq1212"
m = path_table.count("/")
slash =  path_table.split("/",6)[-1]
print('with space - ' + slash)
print('without space - ' +  slash.replace(' ' , ''))
path_table1 = "hdfs://nameservice1/client1/marketrisk/rfds/u-h/data_refresh_scratch/pv_manifest/cobdate=10-OCT-2020/runtype=hsv_1d_car/valcontextid=hsv-10d_vvar/dsloadid=12234/grainid=qwqwq1212"
grain = path_table1.__contains__('dsload')
print(grain)
print('dsloadid' in path_table1)

house_price = 1000000
tenpc = house_price * 0.1
twenpc = house_price * 0.2
good_credit = True
print(house_price , tenpc,twenpc)

if good_credit:
    print (f"Please pay:  {tenpc}")
else: 
    print(f"Please pay: {twenpc}")

print(f"please note, your credit rating is : good_credit" )

'''
'''
print ("hello")
name = input('enter your name ')
print (name)

if len(name) < 3:
    print('Lenght of your name should be more than 2 characters')
elif len(name) > 50:
    print  ('Lenght of your name should be less than 50 characters')
else:
    print('Nice name') 

'''


'''
weight = int(input('enter you weight '))
print (weight)

unit = input('Which Unit of measure would you like to Enter you weight in? Enter p for Pounds or k for kilogram ')
print(unit)

if unit == 'p':
    w = weight / 0.45
    print(f"you weight in kilograms  is - {w} kilos")
elif unit == 'k':
    w = weight * 0.45
    print(f"you weight in kilograms is - {w} kilos" ) 
else:
    print('Enter a valid unit')



i = 1
while i <= 10:
    print('$' * i )
    i = i + 1
    
secret_num = 28
guess_limit = 4
guess_count = 0

while guess_count < guess_limit:
    n = int(input('Guess: '))
    print(n)
    guess_count += 1
    
    if (n == secret_num):
        print('correct')
        break
else:
        print('wrong guess')



start_car = False
stop_car = False
'car_running_status = False'
car_running_status = False
car_stop_status = False

print (start_car , stop_car, car_running_status, car_stop_status)

while not start_car and not car_running_status :
        print('Please start the car')
        strt = int(input("car is not running , press 1 to start"))
        print(strt)
        if strt == 1 and not car_running_status:
            start_car = True
            print('car started')
            car_running_status = True
            car_stop_status = False
        else:
            print("press ONLY 1 to start")
            start_car = False
            car_running_status = False
            car_stop_status = True
        
        while (start_car and car_running_status):
            print("car is running")
            brk = int(input("car is running , press 2 to stop"))
            print(brk)
            if brk == 2:
                print('car stopped')
                car_stop_status = True
                start_car = True
                break
            else:
                print("press ONLY 2 to stop")
                start_car = True
                car_running_status = True
                car_stop_status = False
                
else:
    print("Hope you Enjoyed the ride")


name = input("Enter a name ")
print ('name ' + name.upper())
print ('name ' + name.lower())


m = 0
for i in (1,3,4):
    m += 1

print(m)
     

n = (5,2,5,2,2)
for i in (n):
    print('*' * i )


numbers = (2,2,2,2,5)
for n in numbers:
    d = '' 
    for m in range(n):
        d += 'x'
    print(d)
    


    

n = (2,4,10,103,6,5)
old_no = n[0]

for i in n:
   
    if i > old_no:
        old_no = i
        
print(old_no)
    
   
   
numbers_dict = {
       
       "1":"one",
       "2": "two",
       "3": "three",
       "4": "four",
       "5":"five",
       "6":"six",
       "7":"seven",
       "8":"eight",
       "9":"nine",
       "0":"zero"
   } 

phone = input('enter your phone number ')
print(phone)
op= ''
for n in phone:
        op += numbers_dict.get(n,'?') + ' '
print(op)
    
  '''

emjois = {
       
       ":)" : "😇",
       ":(" : "😞" 
   } 
    
msg = input(">")
eachword = msg.split(' ')
print(eachword)   
allwords = ''
for i in eachword:
    allwords += emjois.get(i,i) + ' '
    print(allwords)
    
    
    
    

