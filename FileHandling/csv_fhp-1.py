import csv
with open('emp3.csv','w', newline='') as f:
    w=csv.writer(f)
    w.writerow(['Eno', 'Ename','Esalary','Ephone'])
    w.writerow([100,'krishna', 2000, 999998877])
    w.writerow([200,'krish', 3000, 9887711111])
    w.writerow([300,'krishna kushwaha', 4000, 9887755555])
    w.writerow([400,'krish kushwaha', 5000, 9887705555])

print('data written successfully ')
