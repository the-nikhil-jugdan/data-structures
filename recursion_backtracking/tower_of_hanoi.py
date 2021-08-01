def move_peg(disc, source='Source', aux='Aux', dest='Destination'):
    if disc == 1:
        print(f"Disc {disc} : {source} -> {dest}")

    else:
        move_peg(disc - 1, source=source, aux=dest, dest=aux)

        print(f"Disc {disc} : {source} -> {dest}")

        move_peg(disc - 1, source=aux, aux=source, dest=dest)


move_peg(4)
