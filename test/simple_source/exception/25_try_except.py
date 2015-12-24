# Tests:
#
#   tryfinallystmt ::= SETUP_FINALLY suite_stmts POP_BLOCK LOAD_CONST COME_FROM suite_stmts_opt END_FINALLY
#   suite_stmts_opt ::= suite_stmts
#   trystmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK try_middle COME_FROM
#   try_middle ::= JUMP_FORWARD COME_FROM except_stmts END_FINALLY COME_FROM
#   except_stmt ::= except_cond1 except_suite
#   except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
#   trystmt ::= SETUP_EXCEPT suite_stmts_opt POP_BLOCK try_middle COME_FROM
#   try_middle ::= JUMP_FORWARD COME_FROM except_stmts END_FINALLY COME_FROM
#   except_cond1 ::= DUP_TOP expr COMPARE_OP jmp_false POP_TOP POP_TOP POP_TOP
try:
    try:
        x = 1
    except AssertionError:
        x = 2

except ImportError:
    x = 3
finally:
    x = 4