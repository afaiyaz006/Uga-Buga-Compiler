from parse import parser
import ply.yacc as yacc
from code_generator import generate_tac,generate_asm
while True:
        try:
            statement = input('')
            ast=yacc.parse(statement) # parsing
            generate_tac(ast)
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        if not statement:
            continue
       


 # tac generation
tac_code=generate_tac.tac_code
print(f";{tac_code}")  
print(generate_asm(tac_code)) # assembly