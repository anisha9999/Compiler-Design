#compiler designed for following hypothetical language
'''

int main()
{
do
{
var=expr+expr;
var=exp;
}
while(T);
return(num);
}
'''
import sys

#list of tokens in the language
tokens=['int','main','(',')','{','}',';','do','var','=','expr','+','expr','exp','while','T','return','num']
print(tokens)

#reference parsing table
parse_table={'0':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'S 3','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'1','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'2','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'1':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'A','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'2':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'S 6','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'4','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'5','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'3':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'R 7','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'4':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'R 0','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'5':{'(':'S 7',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'6':{'(':'R 8',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'7':{'(':'NA',')':'S 8','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'8':{'(':'NA',')':'NA','{':'S 9','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'9':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'S 12','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'10','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'11','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'10':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'S 15','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'13','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'14','VARC':'NA'}             
,             
'11':{'(':'NA',')':'NA','{':'S 16','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'12':{'(':'NA',')':'NA','{':'R 9','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'13':{'(':'NA',')':'NA','{':'NA','}':'S 17','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'14':{'(':'S 18',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'15':{'(':'R 18',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'16':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'S 22','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'19','EX':'20','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'21','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,                 
'17':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'R 1','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}
             
,             
'18':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'S 24','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'23','RETURN':'NA','VARC':'NA'}             
,             
'19':{'(':'NA',')':'NA','{':'NA','}':'S 25','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'20':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'S 22','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'26','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'27','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'21':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'S 29','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'28','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'22':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'R 12','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'23':{'(':'NA',')':'S 30','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'24':{'(':'NA',')':'R 17','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'25':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'S 32',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'31','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'26':{'(':'NA',')':'NA','{':'NA','}':'R 3','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'27':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'S 29','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'33','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'28':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'S 35','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'34','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'29':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'R 14','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'R 14','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'30':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'S 37','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'36','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'31':{'(':'S 38',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'32':{'(':'R 15',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'33':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'S 40','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'39'}             
,             
'34':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'S 42','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'41','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'35':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'R 11','=':'NA','while':'NA',';':'R 11','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'36':{'(':'NA',')':'NA','{':'NA','}':'R 6','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'37':{'(':'NA',')':'NA','{':'NA','}':'R 16','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'R 16','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'R 16','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'38':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'S 44','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'43','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'39':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'S 37','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'45','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'40':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'R 19','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'41':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'S 35','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'46','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'42':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'R 13','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'43':{'(':'NA',')':'S 47','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'44':{'(':'NA',')':'R 10','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'45':{'(':'NA',')':'NA','{':'NA','}':'R 5','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'46':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'S 37','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'48','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'47':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'S 37','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'49','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
 '48':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'R 4','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'NA','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
,             
'49':{'(':'NA',')':'NA','{':'NA','}':'NA','int':'NA','main':'NA','do':'NA','T':'NA','expr':'NA','var':'NA','+':'NA','=':'NA','while':'NA',';':'NA','num':'NA','return':'R 2','exp':'NA','$':'NA','S':'NA','MAI':'NA','ST':'NA','EXP':'NA','EX':'NA','EXPS':'NA','RE':'NA','D':'NA','MAIN':'NA','DO':'NA','COND':'NA','VAR':'NA','ID':'NA','OP':'NA','OR':'NA','WHILE':'NA','SC':'NA','NUM':'NA','RETURN':'NA','VARC':'NA'}             
}
            

# 2 * (number of elements in the grammar)
no_ele={'0':4,'1':14,'2':18,'3':4,'4':12,'5':8,'6':10,'7':2,'8':2,'9':2,'10':2,'11':2,'12':2,'13':2,'14':2,'15':2,'16':2,'17':2,'18':2,'19':2}

#grammar head (non-terminal)
gram_name={'0':'S','1':'MAI','2':'ST','3':'EXP','4':'EX','5':'EXPS','6':'RE','7':'D','8':'MAIN','9':'DO','10':'COND','11':'VAR','12':'ID','13':'OP','14':'OR','15':'WHILE','16':'SC','17':'NUM','18':'RETURN','19':'VARC'}
#error handler
def error_handler(pointer):
    #yet to write the code
    print('hello')
    x=6
    return x

#tokenizer method
def tokenizer(program_string):
    program_string+='$'
    pointer=0
    lis=[] 
    while program_string[pointer] != "$":
        current_string=""
        if program_string[pointer].isalpha():
            current_string+=program_string[pointer]
            pointer+=1
            while program_string[pointer].isalnum() or program_string[pointer]=="_":
                current_string+=program_string[pointer]
                pointer+=1    
            if current_string in tokens:
                lis.append(tokens[tokens.index(current_string)])
            else:
                lis.append('id')    
        elif program_string[pointer].isnumeric():
            current_string+=program_string[pointer]
            pointer+=1
            dot_count=0
            while program_string[pointer].isnumeric() or program_string[pointer]==".":
                if program_string[pointer]==".":
                    dot_count+=1
                current_string+=program_string[pointer]
                pointer+=1
            if dot_count>1:
                x=error_handler(pointer)
                print('Error in Tokenizer Line No. : '+str(x)+' unidentified token '+current_string)
                exit()
            else:
                lis.append('num')
        else:
            if program_string[pointer]!=" " and program_string[pointer]!="\n":
                lis.append(tokens[tokens.index(program_string[pointer])])
                pointer+=1
            else:
                pointer+=1                             
    return lis

#syntax analyzer method
def syntax_analyser(token_list):
    top=0
    stack_token=['0']
    j=len(token_list)
    i=0
    while(i<j):
        x=parse_table[stack_token[top]][token_list[i]].split()
        if(x[0]=='S'):
            print('shift')
            stack_token.append(token_list[i])
            stack_token.append(x[1])
            top+=2
            i+=1
            print(stack_token)
        elif(x[0]=='R'):
            print('reduce')
            stack_token=stack_token[:(top-no_ele[x[1]])+1]
            top-=no_ele[x[1]]
            stack_token.append(gram_name[x[1]])
            top+=1
            stack_token.append(parse_table[stack_token[top-1]][stack_token[top]])
            top+=1
            print(stack_token)    
        elif(x[0]=='NA'):
            print("syntax error..!")
            exit()
        elif(x[0]=='A'):
            print("accepted..!\n")
            exit()
        else:
            break;        
                


        


def main():
    if len(sys.argv) < 2:
        print("Compiler: No input file mentioned...\nUse Syntax cdproj.py <filename>")
        exit()
    program_string=open(sys.argv[1],'r').read() 
    print("\nProgram\n")
    print(program_string)
   
    token_list=tokenizer(program_string)
    print("\nTokens\n")
    print(token_list)
    token_list.append('$')
    print("analysing syntax for the obtained tokens...")
    syntax_analyser(token_list)




try:
    main()
except Exception as e:
    print("Compiler: Unkown compile time Exception occured..."+e)        
