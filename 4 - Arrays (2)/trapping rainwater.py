# program to calculate trapped rainwater:

height = [4,2,0,6,3,2,5]

def trapped_rainwater(h):
    # calculate the auxilarry arrays for lmax and rmax boundary:
    # calculate left max
    lmax = [0]*len(h)
    lmax[0] = h[0]
    for i in range(1,len(h)):
        lmax[i] = max(h[i],lmax[i-1])
    print(lmax)

    # calculate right max
    rmax = [0] * len(h)
    rmax[-1] = height[-1]
    for i in range((len(h)-2),-1, -1):
        rmax[i] = max(h[i], rmax[i+1])
    print(rmax)
    trapped_water = 0
    for i in range(0,len(h)):
        water_lev = min(rmax[i],lmax[i])
        trapped_water += water_lev - h[i]
    return trapped_water


print(trapped_rainwater(height))