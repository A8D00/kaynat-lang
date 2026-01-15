# compiler/ir.py
# التمثيل الوسيط (IR) للغة الكيانات
# هذا المستوى مستقل عن العربية ومستقل عن المعمارية

# ---------- تعليمات IR الأساسية ----------

class IRInstruction:
    pass


class IRFunction(IRInstruction):
    def __init__(self, name):
        self.name = name
        self.body = []


class IRReturn(IRInstruction):
    def __init__(self, value):
        self.opcode = 0b11111111   # opcode الخاص بـ RETURN
        self.value = format(value, "08b")  # operand = 8 bits

class IRLoadConst(IRInstruction):
    def __init__(self, value):
        self.value = value


class IRAdd(IRInstruction):
    pass


class IRSub(IRInstruction):
    pass

class IRStore(IRInstruction):
    def __init__(self, address):
        self.address = address


class IRLoadVar(IRInstruction):
    def __init__(self, address):
        self.address = address

# ---------- محوّل AST → IR ----------

    class IRBuilder:
    def __init__(self):
        self.variables = {}      # اسم المتغير → عنوان
        self.next_address = 0    # العنوان التالي
   
    def get_var_address(self, name):
    if name not in self.variables:
        self.variables[name] = self.next_address
        self.next_address += 1
    return self.variables[name]
    
    def build(self, program):
        """
        program: عقدة Program من الـ AST
        """
        functions = []
        for fn in program.functions:
            functions.append(self.build_function(fn))
        return functions

 def build_function(self, fn):
    ir_fn = IRFunction(fn.name)

    for stmt in fn.body:

        if stmt.__class__.__name__ == "Assignment":
            addr = self.get_var_address(stmt.name)

            if stmt.value.__class__.__name__ == "Number":
                ir_fn.body.append(IRLoadConst(stmt.value.value))
                ir_fn.body.append(IRStore(addr))

        elif stmt.__class__.__name__ == "Return":

            if stmt.value.__class__.__name__ == "Number":
                ir_fn.body.append(IRLoadConst(stmt.value.value))
                ir_fn.body.append(IRReturn(stmt.value.value))

            elif stmt.value.__class__.__name__ == "Identifier":
                addr = self.get_var_address(stmt.value.name)
                ir_fn.body.append(IRLoadVar(addr))
                ir_fn.body.append(IRReturn(0))

    return ir_fn

        # حاليًا ندعم: دالة تحتوي على return واحد فقط
        ret_value = fn.body.value.value

# نحول القيمة إلى تمثيل ثنائي بسيط (8-bit)
binary_value = format(ret_value, "08b")

ir_fn.body.append(IRReturn(binary_value))

        return ir_fn
