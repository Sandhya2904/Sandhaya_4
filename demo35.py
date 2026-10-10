import time
class vendor:
    def __init__(self,vName,vGST):
        self.vName = vName
        self.vGST = vGST
        print(f'Vendor {self.vName} enrollment is done')
    def billing(self,pName,pQty=0,pCost=0.0):
        self.pName = pName
        self.pQty = pQty
        self.pCost = pCost
        self.total = self.pCost * self.pQty
        self.tax = self.total * 0.18
        self.gs = self.total + self.tax
        s1=f'{self.vName}\t{self.vGST}\t{self.pName}\t{self.pQty}'
        s2=f'\t{self.pCost}\t{self.total}\t{self.gs}'
        s3=f'\t{time.ctime()}\n\n'
        with open('vendor_prods.log','a') as wobj:
            wobj.write(s1+s2+s3)
