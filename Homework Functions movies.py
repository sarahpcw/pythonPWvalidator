
Create a file with a class with 5 functions : 
1. function name: calcTicket
Input parameter: day
Calculate the singleTicketPrice: 
 mon : singleTicketPrice = 0
 tue, wed , thu: singleTicketPrice = £10
 fri, sat : singleTicketPrice = £20 
 sun: singleTicketPrice = £30 
Return value: singleTicketPrice (float)

2. function name: calcA
 Input parameters: number of adults and singleTicketPrice
 adultCost = number of adults * singleTicketPrice
 Return value: adultCost (float)

3. function name: calcC
 Input parameters: number of childern and singleTicketPrice
 Children pay half
 Return value: childrenCost (float)

4. function name: calcP
 Input parameters: number of pensioners and singleTicketPrice
 Pensioners pay 75%
 Return value: pensionersCost (float)

5. function name: printTotalPrice
 Input parameters: totalTicketPrice
 Return value: None
 To do: 
If their totalTicketPrice is less than and equals £200,
 display “totalTicketPrice is …
 else 
 Print “Sales over £200. We do not allow large groups into the cinema 
”. 


in the execute file  
1. Find out from the end-user how many adults, children and pensioners are in a party.
2. Find out from the end-user which day they want to see a movie.

 Call the function calcTicket to calculate singleTicketPrice
 If there are adults in the party, call function calcA to the get the adultCost
 If there are children in the party, call function calcC to the get the childrenCost
 If there are pensioners in the party, call function calcP to the get the pensionersCost
 totalTicketPrice = adultCost + childrenCost + pensionersCost
 call the printTotalPrice function

