import time
import os

def insertion_sort(array: list) -> list:
   
    n = len(array)
    sorted_array = list(array)

    start_time = time.perf_counter()

    for i in range(1, n):
        key = sorted_array[i]
        j = i - 1
        while j >= 0 and sorted_array[j] > key:
            sorted_array[j + 1] = sorted_array[j]
            j -= 1
        sorted_array[j + 1] = key

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Tempo de execução do Insertion Sort: {elapsed_time:.6f} segundos")
    return sorted_array

def read_numbers_from_file(filename: str) -> list:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Erro: O arquivo '{filename}' não foi encontrado.")
    
    numbers = []
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, 1):
            try:
                numbers.append(int(line.strip()))
            except ValueError:
                print(f"Aviso: Linha {line_num} no arquivo '{filename}' não é um número inteiro válido e será ignorada: '{line.strip()}'")
                continue
    return numbers

def write_numbers_to_file(filename: str, numbers: list):
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(map(str, numbers)))
    except IOError as e:
        print(f"Erro ao escrever no arquivo '{filename}': {e}")

def main():
    input_file = "num.100000.4.in"
    output_file = "num.10000.4.out"

    print(f"Iniciando a leitura do arquivo: '{input_file}'...")
    try:
        numbers = read_numbers_from_file(input_file)
        print(f"Leitura concluída. Foram lidos {len(numbers)} números.")
    except (FileNotFoundError, ValueError) as e:
        print(e)
        return

    if not numbers:
        print("O arquivo de entrada está vazio ou não contém números válidos. Nenhuma ordenação será realizada.")
        return

    print("Iniciando a ordenação com Insertion Sort...")
    sorted_numbers = insertion_sort(numbers)

    print(f"Iniciando a escrita dos números ordenados no arquivo: '{output_file}'...")
    write_numbers_to_file(output_file, sorted_numbers)
    print(f"Números ordenados salvos em '{output_file}'.")

if __name__ == "__main__":
    main()