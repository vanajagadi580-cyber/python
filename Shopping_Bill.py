shirt=400
dress=700
pant=300
tshirt=300
print('**Welcome to best shoping mall**')
cname=input('Enter customer name:')
cphno= int(input('Enter Phno:'))
shirts=int(input('Enter no of shirts selected'))
pants=int(input('Enter no of pants selected'))
dresses=int(input('Enter no of dresses selected'))
tshirts=int(input('Enter no of t-shirts selected'))
bill=(shirt*shirts)+(pant*pants)+(dress*dresses)+(tshirt*tshirts)
if bill>=7000:
    disc=bill*25/100
elif bill>=5000:
    disc=bill*20/100
elif bill>=3000:
    disc=bill*10/100
elif bill>=1000:
    disc=bill*5/100
else:
    disc=bill*3/100
tbill=bill-disc
gst=tbill*12/100
obill=tbill+gst
print('customer name:',cname)
print('customer phno:',cphno)
print('bill:',bill)
print('discount:',disc)
print('gst 12%:',gst)
print('bill to be paid:',obill)
print('**THANK U! VISIT AGAIN**')
