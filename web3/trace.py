from web3.module import (
    Module,
)


class Trace(Module):

    defaultBlock = "latest"

    def call(self, transaction, types, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "trace_call",
            [
                transaction,
                types,
                block_identifier,
            ],
        )

    def rawTransaction(self, rtransaction, types):
        return self.web3.manager.request_blocking(
            "trace_rawTransaction",
            [
                rtransaction,
                types,
            ],
        )

    def replayTransaction(self, transaction, types):
        return self.web3.manager.request_blocking(
            "trace_replayTransaction",
            [
                transaction,
                types,
            ],
        )

    def block(self, block_identifier=None):
        if block_identifier is None:
            block_identifier = self.defaultBlock
        return self.web3.manager.request_blocking(
            "trace_block",
            [
                block_identifier,
            ],
        )

    def filter(self, tfilter):
        return self.web3.manager.request_blocking(
            "trace_filter",
            [
                tfilter,
            ],
        )

    def get(self, transaction, indices):
        return self.web3.manager.request_blocking(
            "trace_get",
            [
                transaction,
                indices,
            ],
        )

    def transaction(self, transaction):
        return self.web3.manager.request_blocking(
            "trace_transaction",
            [
                transaction,
            ],
        )
