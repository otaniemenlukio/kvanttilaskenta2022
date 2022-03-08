def revbits(n):
    """Iterates over the bits in the number in reverse: lowest-order bit first. Does not add zero padding
    
    n -- number to iterate over
    """
    while n:
        yield n & 1
        n >>= 1

def get_rich_counts(result):
    """Returns the measurements containing counts and measurements for each register separately    
    
    result -- qiskit Result
    """
    rich_counts = {}
    for key in range(len(result.results)):
        rich_counts[key] = []
        exp = result._get_experiment(key)
        header = exp.header.to_dict()

        if "counts" in result.data(key).keys():
            bitlistcounts = [(list(revbits(int(k, 16))), counts) for k, counts in result.data(key)["counts"].items()]
            for bitlistcount in bitlistcounts:
                bitlist, counts = bitlistcount
                labeled = { "counts": counts }
                for label in set(dict(header['clbit_labels']).keys()):
                    labeled[label] = []
                
                for i in range(header['memory_slots']):
                    bit = bitlist[i] if i < len(bitlist) else 0
                    labeled[header['clbit_labels'][i][0]].append(bit)
                
                rich_counts[key].append(labeled)
        else:
            raise QiskitError(f'No counts for experiment "{repr(key)}"')

    return rich_counts