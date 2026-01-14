import platform

def get_target():
    arch = platform.machine()

    if arch in ("x86_64", "AMD64"):
        from targets.x86_64_linux import generate_exit
        return generate_exit

    if arch in ("aarch64", "arm64"):
        from targets.arm64_linux import generate_exit
        return generate_exit

    raise RuntimeError(f"المعمارية غير مدعومة: {arch}")
