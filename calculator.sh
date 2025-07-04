echo "Please enter two numbers"
read num1 
read num2 

while [[ !$num1 =~ ^[0-9]+$]] || [[! $num2 =~ ^[0-9]+$]]
do 
echo "Make sure input values are numeric, please enter both numbers again"
read num1 
read num2 
done 

echo "Please choose an operation:"
read -p "choose if you want to add(+),substract(-),multiply(*), or divide(/):"
operavar ]]


do 
read -p "choose if you want to add(+), substract(-), multiply(*), or divide(/):"
done 

if [[$operavar = "+"]]
then 
echo "addition"
sub = $num1 * $num2 = $mult"
echo "$num1 - $num2 = $sub"
then 
echo "substraction"
sub = "$((num1 - $num2))
echo "$num1 - $num2 = $sub"
elif [[ $operavar = "/"]]
then 
echo "divide"
if [$num2 -eq 0]
then 
echo "denominator cannot be zero"
else 
div =($num1 / $num2))
echo "$num1 / $num2 = $div"
fi 
fi