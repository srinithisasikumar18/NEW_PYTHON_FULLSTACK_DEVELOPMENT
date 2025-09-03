employees=[{"eid":1,"ename":"Lillian","gender":"Female"},
{"eid":2,"ename":"Jard","gender":"Male"},
{"eid":3,"ename":"Berty","gender":"Female"},
{"eid":4,"ename":"Lolly","gender":"Female"},
{"eid":5,"ename":"Fedora","gender":"Female"},
{"eid":6,"ename":"Ali","gender":"Female"},
{"eid":7,"ename":"Ronda","gender":"Female"},
{"eid":8,"ename":"Oralie","gender":"Female"},
{"eid":9,"ename":"Lewie","gender":"Male"},
{"eid":10,"ename":"Levey","gender":"Male"},
{"eid":11,"ename":"Cornie","gender":"Male"},
{"eid":12,"ename":"Octavia","gender":"Female"},
{"eid":13,"ename":"Gizela","gender":"Female"},
{"eid":14,"ename":"Wake","gender":"Male"},
{"eid":15,"ename":"Lori","gender":"Female"},
{"eid":16,"ename":"Nero","gender":"Male"},
{"eid":17,"ename":"Annabela","gender":"Female"},
{"eid":18,"ename":"Rona","gender":"Female"},
{"eid":19,"ename":"Bertrand","gender":"Male"},
{"eid":20,"ename":"Horton","gender":"Male"},
{"eid":21,"ename":"Kit","gender":"Female"},
{"eid":22,"ename":"Kathryn","gender":"Female"},
{"eid":23,"ename":"Vita","gender":"Female"},
{"eid":24,"ename":"Allsun","gender":"Female"},
{"eid":25,"ename":"Beulah","gender":"Female"},
{"eid":26,"ename":"Maryann","gender":"Agender"},
{"eid":27,"ename":"Durand","gender":"Male"},
{"eid":28,"ename":"Manny","gender":"Male"},
{"eid":29,"ename":"Sharity","gender":"Female"},
{"eid":30,"ename":"Hewett","gender":"Male"},
{"eid":31,"ename":"Yoko","gender":"Female"},
{"eid":32,"ename":"Elane","gender":"Female"},
{"eid":33,"ename":"Shamus","gender":"Male"},
{"eid":34,"ename":"Fabiano","gender":"Male"},
{"eid":35,"ename":"Fawnia","gender":"Female"},
{"eid":36,"ename":"Joeann","gender":"Female"},
{"eid":37,"ename":"Hermia","gender":"Bigender"},
{"eid":38,"ename":"Lorain","gender":"Female"},
{"eid":39,"ename":"Everett","gender":"Male"},
{"eid":40,"ename":"Galven","gender":"Male"},
{"eid":41,"ename":"Putnam","gender":"Male"},
{"eid":42,"ename":"Jerry","gender":"Male"},
{"eid":43,"ename":"Berke","gender":"Male"},
{"eid":44,"ename":"Scotty","gender":"Genderfluid"},
{"eid":45,"ename":"Lauryn","gender":"Female"},
{"eid":46,"ename":"Mureil","gender":"Female"},
{"eid":47,"ename":"Giulio","gender":"Male"},
{"eid":48,"ename":"Christie","gender":"Female"},
{"eid":49,"ename":"Nels","gender":"Male"},
{"eid":50,"ename":"Jaime","gender":"Female"},
{"eid":51,"ename":"Pamela","gender":"Genderqueer"},
{"eid":52,"ename":"Danell","gender":"Female"},
{"eid":53,"ename":"Mureil","gender":"Female"},
{"eid":54,"ename":"Nixie","gender":"Female"},
{"eid":55,"ename":"Audrey","gender":"Female"},
{"eid":56,"ename":"Elvira","gender":"Female"},
{"eid":57,"ename":"Chery","gender":"Female"},
{"eid":58,"ename":"Hestia","gender":"Female"},
{"eid":59,"ename":"Torrance","gender":"Male"},
{"eid":60,"ename":"Garv","gender":"Male"},
{"eid":61,"ename":"Lenora","gender":"Female"},
{"eid":62,"ename":"Kippy","gender":"Female"},
{"eid":63,"ename":"Ogdon","gender":"Male"},
{"eid":64,"ename":"Mildrid","gender":"Female"},
{"eid":65,"ename":"Cyndy","gender":"Female"},
{"eid":66,"ename":"Briano","gender":"Male"},
{"eid":67,"ename":"Nadia","gender":"Female"},
{"eid":68,"ename":"Keir","gender":"Male"},
{"eid":69,"ename":"Abeu","gender":"Male"},
{"eid":70,"ename":"Adriane","gender":"Female"},
{"eid":71,"ename":"Leonanie","gender":"Female"},
{"eid":72,"ename":"Vasili","gender":"Male"},
{"eid":73,"ename":"Cathlene","gender":"Female"},
{"eid":74,"ename":"Anne-corinne","gender":"Female"},
{"eid":75,"ename":"Bea","gender":"Female"},
{"eid":76,"ename":"Bendick","gender":"Male"},
{"eid":77,"ename":"Corty","gender":"Male"},
{"eid":78,"ename":"Mordy","gender":"Male"},
{"eid":79,"ename":"Michell","gender":"Female"},
{"eid":80,"ename":"Elka","gender":"Female"},
{"eid":81,"ename":"Trish","gender":"Female"},
{"eid":82,"ename":"Idell","gender":"Female"},
{"eid":83,"ename":"Nananne","gender":"Female"},
{"eid":84,"ename":"Cecilius","gender":"Male"},
{"eid":85,"ename":"Yasmin","gender":"Female"},
{"eid":86,"ename":"Darice","gender":"Female"},
{"eid":87,"ename":"Jeannie","gender":"Female"},
{"eid":88,"ename":"Reta","gender":"Female"},
{"eid":89,"ename":"Margeaux","gender":"Female"},
{"eid":90,"ename":"Annaliese","gender":"Female"},
{"eid":91,"ename":"Hedy","gender":"Female"},
{"eid":92,"ename":"Jorge","gender":"Male"},
{"eid":93,"ename":"Herman","gender":"Male"},
{"eid":94,"ename":"Erinna","gender":"Female"},
{"eid":95,"ename":"Ravid","gender":"Male"},
{"eid":96,"ename":"Dorelia","gender":"Female"},
{"eid":97,"ename":"Cariotta","gender":"Female"},
{"eid":98,"ename":"Rabi","gender":"Male"},
{"eid":99,"ename":"Zaccaria","gender":"Male"},
{"eid":100,"ename":"Briney","gender":"Genderfluid"}]
# for employee in employees:
#     # print(employee)
#     print("employee name",employee['ename'])
# for employee in employees:
#     if employee['gender']=='Male':
#         print("Male employee",employee['ename'])

# for emp in employees:
#     if emp["gender"]=="Female":
#         print("Female Employees",emp["ename"])
male_emp=0
female_emp=0
other_emp=0
for emp in employees:
    if emp["gender"]=="Male":
        male_emp+=1
    if emp["gender"]=="Female":
        female_emp+=1
    if emp["gender"]!="Male","Female":
        other_emp+=1



print("Total male employess are:",male_emp)
print("Total female employess are:",female_emp)
print("Other employee:",other_emp)