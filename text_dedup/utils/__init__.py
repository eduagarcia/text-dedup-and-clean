#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-12-26 15:42:09
# @Author  : Chenghao Mou (mouchenghao@gmail.com)

from text_dedup.utils.add_args import add_bloom_filter_args
from text_dedup.utils.add_args import add_exact_hash_args
from text_dedup.utils.add_args import add_io_args
from text_dedup.utils.add_args import add_meta_args
from text_dedup.utils.add_args import add_minhash_args
from text_dedup.utils.add_args import add_sa_args
from text_dedup.utils.add_args import add_simhash_args
from text_dedup.utils.hashfunc import sha1_hash
from text_dedup.utils.hashfunc import xxh3_hash
from text_dedup.utils.add_args import add_fix_text_args
from text_dedup.utils.timer import Timer
from text_dedup.utils.tokenization import ngrams
from text_dedup.utils.union_find import UnionFind
from text_dedup.utils.load_datasets import load_dataset
from text_dedup.utils.utils import (
    deep_update
)

__all__ = [
    "add_bloom_filter_args",
    "add_exact_hash_args",
    "add_io_args",
    "add_meta_args",
    "add_minhash_args",
    "add_sa_args",
    "add_simhash_args",
    "add_fix_text_args",
    "Timer",
    "ngrams",
    "UnionFind",
    "sha1_hash",
    "xxh3_hash",
    "load_dataset",
    "deep_update"
]
