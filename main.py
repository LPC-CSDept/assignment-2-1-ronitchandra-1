def main():
    
    nmale = int(input("Enter the number of males: "))
    nfem = int(input("Enter the number of females: "))
    total = nmale + nfem
    m_perc = nmale / total * 100
    f_perc = nfem / total * 100
    print(f"Total:\t {total}")
    print(f"Males and Females: \t {nmale} \t {nfem}")
    print(f"Percentages of Males and Females: \t {m_perc:.2f}% \t {f_perc:.2f}%")
    return m_perc, f_perc


if __name__ == '__main__':
    main()
