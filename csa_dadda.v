//carry save adder -- for implementing dadda multiplier
//csa for use of half adder and full adder.

module csa_dadda(A,B,Cin,Y,Cout);
input A,B,Cin;
output Y,Cout;
    
assign Y = A^B^Cin;  // 2 xor-gate
assign Cout = (A&B)|(A&Cin)|(B&Cin); 
//Option 1: 3 and-gate and 2 or-gate 
//Option 2: otherwise use another option: 1 and-nor gate ,1 and gate ,1 or gate,1 not gate
//************************************************//
// the second score is total 20, while the first needs 30, the second is better
    
endmodule
