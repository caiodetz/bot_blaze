from PyInstaller.__main__ import run
import os

def build_executable(script_path, output_dir="dist", onefile=True, windowed=False, icon_path=None):
    if not os.path.exists(script_path):
        print(f"Erro: O arquivo {script_path} não foi encontrado.")
        return
    args = [
        script_path,                     # Caminho do script
        f"--distpath={output_dir}",      # Diretório de saída
    ]

    if onefile:
        args.append("--onefile")
    if windowed:
        args.append("--noconsole")
    if icon_path and os.path.exists(icon_path):
        args.append(f"--icon={icon_path}")
    try:
        run(args)
        print(f"Build concluído com sucesso! Executável criado em '{os.path.abspath(output_dir)}'.")
    except Exception as e:
        print(f"Erro ao criar o executável: {e}")

# Exemplo de uso
if __name__ == "__main__":
    script = "main.py"  # Substitua pelo caminho do seu script Python
    build_executable(script, onefile=True, windowed=True, icon_path="icon.ico")
