
# Generate Three-Address Code
def generate_tac(node):
    if isinstance(node, tuple):
        
        op = node[0]
        left = generate_tac(node[1])
        right = generate_tac(node[2])
        output=f'{left} {op} {right}'
       
        temp = f"t{generate_tac.temp_counter}"
       
        generate_tac.temp_counter += 1
            
        if op=="EQUAX":
            #print(f"{temp} = {right}")
            #print(f"{left} = {temp}")
            
            generate_tac.tac_code[generate_tac.temp_counter-1]=f"{temp} = {right}"
        else:
            #print(f"{temp} = {left} {op} {right}")
            generate_tac.tac_code[generate_tac.temp_counter-1]=f"{temp} = {left} {op} {right}"
            generate_tac.cache[output]=temp
            
        return temp
    else:
        return str(node)
    
# Generate 8086 assembly code
def generate_asm(tac_code:dict[int:str]):
    header=[
    ]
    body=[
        'start:',
    ]
    
    
    for no,line in tac_code.items():
        tokens=line.split(' ')
        if len(tokens)==3:
            header.append(f"{tokens[0]}: DW 0")
        elif len(tokens)==5 and tokens[1]=='=':
            var=tokens[0]
            header.append(f"{var}: DW 0")
            if tokens[0][0]=='t':
                tokens[0]=f'word {tokens[0]}'
            if tokens[2][0]=='t':
                tokens[2]=f'word {tokens[2]}'
            if tokens[4][0]=='t':
                tokens[4]=f'word {tokens[4]}'
            if tokens[3]=='+':
                body.append(f"MOV AX,{tokens[2]}")
                body.append(f"ADD AX,{tokens[4]}")
                body.append(f"MOV word {var},AX")
            elif tokens[3]=='-':
                body.append(f"MOV AX,{tokens[2]}")
                body.append(f"SUB AX,{tokens[4]}")
                body.append(f"MOV word {var},AX")

            elif tokens[3]=='*' or tokens[3]=='/':
                if tokens[2][0]=='w':
                    body.append(f"MOV AX,{tokens[2]}")
                    body.append(f"MOV BX,{tokens[4]}")
                    if tokens[3]=='*':
                        body.append(f"MUL BL")
                    if tokens[3]=='/':
                        body.append(f"DIV BL")
                    body.append(f"MOV word {var},AX")
                elif tokens[4][0]=='w':
                    body.append(f"MOV AX,{tokens[4]}")
                    body.append(f"MOV BX,{tokens[2]}")
                    if tokens[3]=='*':
                        body.append(f"MUL BL")
                    if tokens[3]=='/':
                        body.append(f"DIV BL")
                    body.append(f"MOV word {var},AX")
                else:
                    body.append(f"MOV AX,{tokens[2]}")
                    body.append(f"MOV BX,{tokens[4]}")
                    if tokens[3]=='*':
                        body.append(f"MUL BL")
                    if tokens[3]=='/':
                        body.append(f"DIV BL")
                    body.append(f"MOV word {var},AX")
                
    tail=[
    ]
    final=[
        "\n".join(header),
        "\n".join(body),
       
    ]
    final="\n".join(final)
    return final
    



generate_tac.temp_counter = 1
generate_tac.cache={}
generate_tac.tac_code={}
