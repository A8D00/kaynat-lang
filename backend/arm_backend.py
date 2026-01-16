from backend.backend_base import Backend

class ARMBackend(Backend):
    def emit(self, ir):
        return f"""
        MOV R0, #{ir.state}
        ADD R0, R0, #{ir.increment}
        """
