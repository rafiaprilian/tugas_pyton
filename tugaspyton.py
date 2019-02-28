Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print ("hello world");
hello world
>>> 
>>> print (1+2)
3
>>> print (8186-7365)
821
>>> print (86*700)
60200
>>> print (8186/7365)
1.1114731839782757
>>> print (8186-7365)
821
>>> print ("ANTRIAN"+2);
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print ("ANTRIAN"+2);
TypeError: can only concatenate str (not "int") to str
>>> print ("ANTRIAN +2");
ANTRIAN +2
>>> ("ANTRIAN 2");
'ANTRIAN 2'
>>> ("ANTRIAN" 2);
SyntaxError: invalid syntax
>>> ("ANTRIAN 2");
'ANTRIAN 2'
>>> ("ANTRIAN",2);
('ANTRIAN', 2)
>>> PRINT ("ANTRIAN",2);
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    PRINT ("ANTRIAN",2);
NameError: name 'PRINT' is not defined
>>> print ("ANTRIAN",2);
ANTRIAN 2
>>> a=1
>>> ("ANTRIAN",2);
('ANTRIAN', 2)
>>> a=1;
>>> b=2;
>>> print ("a+b");
a+b
>>> print (a+b);
3
>>> print ("lingga")("rpl xi 4")
lingga
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print ("lingga")("rpl xi 4")
TypeError: 'NoneType' object is not callable
>>> print ("lingga")	print ("rpl xi 4");
SyntaxError: invalid syntax
>>> print a = "lingga"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a = "lingga")?
>>> print a = "lingga" b = "rpl xi 4" (a+b);
SyntaxError: invalid syntax
>>> a = "lingga"
>>> b = "rpl"
>>> print ("lingga\nrpl")
lingga
rpl
>>> print ("lingga"); print ("rpl xi 4");
lingga
rpl xi 4
>>> c ="11706114"
>>> d = "smk wikrama"
>>> print (a); (b); (c); (d);
lingga
'rpl'
'11706114'
'smk wikrama'
>>> print (a+b+c+d);
linggarpl11706114smk wikrama
>>> print (a b c d);
SyntaxError: invalid syntax
>>> print (a, '/n'b, '/n'c, '/n',d);
SyntaxError: invalid syntax
>>> print (a, '\n'b, '\n'c, '\n',d);
SyntaxError: invalid syntax
>>> print (a, '\n'b, '\n'c, '\n',d'\n');
SyntaxError: invalid syntax
>>> print (a)'n', (b)'n', (c)'n', (d)'n';
SyntaxError: invalid syntax
>>> print (a)'\n', (b)'\n', (c)'\n', (d)'\n';
SyntaxError: invalid syntax
>>> print (a, "/n"b, "/n"c, "/n",d);
SyntaxError: invalid syntax
>>> print (a, "\n"b, "\n"c, "n",d);
SyntaxError: invalid syntax
>>> print (a, "\n"b, "\n"c, "\n",d),"\n";
SyntaxError: invalid syntax
>>> print (a, "\n",b, "\n",c, "n",d);
lingga 
 rpl 
 11706114 n smk wikrama
>>> print (a,"\n",b,"\n",c,"n",d);
lingga 
 rpl 
 11706114 n smk wikrama
>>> 
