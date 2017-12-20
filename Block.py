import hashlib
import uuid

class Block(object):
    def __init__(self, data = None, previous_hash = None):
        self.identifier = uuid.uuid4().hex
        self.nonce = None
        self.data = data
        self.previous_hash = previous_hash

    def hash(self, nonce = None):
        message = hashlib.sha256()
        message.update(self.identifier.encode('utf-8'))
        message.update(str(nonce).encode('utf-8'))
        message.update(str(self.data).encode('utf-8'))
        message.update(str(self.previous_hash).encode('utf-8'))

        return message.hexdigest()

    def hash_is_valib(self, the_hash):
        return the_hash.startswith('0000')

    def __repr__(self):
        return 'Block<Hash: {}, Nonce: {}>'.format(self.hash(), self.nonce)

    def mine(self):
        cur_nonce = self.nonce or 0

        while True:
            the_hash = self.hash(nonce = cur_nonce)
            if self.hash_is_valib(the_hash):
                self.nonce = cur_nonce
                break
            else:
                cur_nonce += 1

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.blocks = {}

    def add_block(self, new_block):
        previous_hash = self.head.hash(self.head.nonce) if self.head else None
        new_block.previous_hash = previous_hash

        self.blocks[new_block.identifier] = {
            'block': new_block,
            'previous_hash': previous_hash,
            'previous': self.head
        }
        self.head = new_block

    def __repr__(self):
        num_existing_blocks = len(self.blocks)
        return 'Blockchain<{} Blocks, Head: {}>'.format(num_existing_blocks, self.head.identifier if self.head else None)
