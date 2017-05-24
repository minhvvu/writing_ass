# text_parser module for parsing text file into pair
# of close words with weight denote it's distance

from nltk.corpus import PlaintextCorpusReader

def load_data(data_root, file_ext):
    """
    Load all text file in directory `data_root` with extension as `file_ext`.
    Return list of all sentences.
    """
    return PlaintextCorpusReader(data_root, file_ext).sents()


def make_pairs(sent, dist):
    """
    For each word in sentence `sent`, consider its neighbors in window_size `ws`.
    Assign each neighbor according to the distribution `dist` = [dist1, dist2, dist3,...]

    left3, left2, left1, word, right1, right2, right3
    dist1, dist2, dist3,     , dist3,  dist2,  dist1

    Return an iterator over 2 types of pair:
        (left_i, word, dist_i) and
        (word, right_i, dist_i)
    """
    n = len(sent)
    ws = min(len(dist), n-1)
    pairs = []
    for i in range(n-1):
        pairs += [(sent[i], sent[i+w+1], dist[w]) for w in range(ws) if i+w+1 < n]
    return pairs


def parse_to_pairs(data_root='.', file_ext=r'.*\.txt', dist=[1, .75, .25]):
    sentences = load_data(data_root, file_ext)
    pairs = [make_pairs(sent, dist) for sent in sentences ]
    return pairs


def main():
    distribution = [1, 0.5, 0.2]
    data_root = '/home/minhvu/Data/dummy/'
    pairs = parse_to_pairs(data_root, dist=distribution)
    for p in pairs[:3]: print(p)

if __name__ == '__main__':
    main()
