"""
duita iterables er onurup element er tuple create kore 
"""
f1=zip([1,2,3],[4,5,6])#kichu return kore,create kore zip object
l=list(f1)#[(1,4),(2,5),(3,6)]
d=dict(f1)#{1:4,2:5,3:6}
l1=[(1,2),(3,4),(1,6)]
l2=list(zip(*l1))
#* prothome l1 ke unpack korbe. individual element abar ekekta tuple
#zip((1,2),(3,4),(1,6))
#zip protita tuple er first element niye new ekta tuple create korbe
#l2=[(1,3,1),(2,4,6)]

#zip complex

midterm=[80,90,100]
final=[85,98,70]
students=["k","h","m"]
#we want final grades={"k":85,"h":98,"m":100}

final_grades={x[0]: max(x[1],x[2]) for x in zip(students,midterm,final)}
#map use kore
final_grades= dict(
    zip(
        students, 
        map(
            lambda x: max(x), zip(midterm,final)
        )
    )
)
