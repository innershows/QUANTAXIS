import datetime
import unittest

import pandas as pd

from QUANTAXIS import QUANTAXIS as QA
from QUANTAXIS.QAData import (QA_DataStruct_Index_day, QA_DataStruct_Index_min,
                              QA_DataStruct_Stock_block,
                              QA_DataStruct_Stock_day, QA_DataStruct_Stock_min,
                              QA_DataStruct_Stock_transaction)
from QUANTAXIS.QAData.base_datastruct import _quotation_base
from QUANTAXIS.QAFetch.QAQuery import (QA_fetch_index_day, QA_fetch_index_min,
                                       QA_fetch_stock_day, QA_fetch_stock_full,
                                       QA_fetch_stock_min)
from QUANTAXIS.QAFetch.QAQuery_Advance import QA_fetch_stock_day_adv
from QUANTAXIS.QAUtil.QAParameter import (DATABASE_TABLE, DATASOURCE,
                                          FREQUENCE, MARKET_TYPE,
                                          OUTPUT_FORMAT)


class quotation_base_test(unittest.TestCase):
    '''

    '''
    def test_quotation_base_class(self):


        df_from_Tdx = QA.QA_quotation('300439', '2018-04-01', '2018-04-10', frequence=FREQUENCE.DAY,
                                   market=MARKET_TYPE.STOCK_CN, source=DATASOURCE.TDX, output=OUTPUT_FORMAT.DATAFRAME)



        # for iRow in range((df_from_Tdx)):
        #     print(iRow)

    def test_quotation_base_class_iter_(self):
        qaDAStruct = QA_fetch_stock_day_adv('300439')

        for iRow in qaDAStruct:
            print(iRow)

        iterObj = qaDAStruct.__iter__()
        a = type(iterObj)
        print(a)
        i = iterObj.__next__()
        print(i)
        i = iterObj.__next__()
        print(i)
        i = iterObj.__next__()
        print(i)

    def do0_ReverseAttributes_test(self):
        qaDAStruct = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-10")
        rev_qaDAStruct = reversed(qaDAStruct)
        list1 = []
        for iRow in qaDAStruct:
            print(iRow)
            list1.append(iRow)
        print('--------------')
        list2 = []
        for iRowRev in rev_qaDAStruct:
            print(iRowRev)
            list2.append(iRowRev)
        print('--------------')

    def test_quotation_base_class_reverse_(self):

        #?????? reverse
        self.assertRaises(NotImplementedError,self.do0_ReverseAttributes_test)


    def test_quotation_base_class_add_(self):
        qaDAStruct0 = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-10")

        qaDAStruct0.show()

        qaDAStruct1 = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-05")
        qaDAStruct2 = QA_fetch_stock_day_adv('300439', start="2018-01-06", end="2018-01-10")
        qaDAStruct3 = qaDAStruct1 + qaDAStruct2

        qaDAStruct3.show()

        # ????todo ??????????????????????????????
        b = qaDAStruct0().equals(qaDAStruct3())
        #self.assertEqual(b, True)

        # ????todo ??????????????????????????????
        # ????????????????????? ??? ????????? ?????? __eq__?????????
        # self.assertEqual( qaDAStruct0 , qaDAStruct3)


        list1 = []
        for iRow1 in qaDAStruct0:
            list1.append(iRow1)

        list2 = []
        for iRow2 in qaDAStruct0:
            list2.append(iRow2)

        len1 = len(list1)
        len2 = len(list2)

        for iIndex in range(len1):
            aRow = list1[iIndex]
            bRow = list2[iIndex]

            # ????????????????????????
            v = aRow.equals(bRow)
            self.assertEqual(v, True)



    def test_quotation_base_class_sub_(self):

        qaDAStruct0 = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-10")

        qaDAStruct0.show()

        qaDAStruct1 = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-05")
        qaDAStruct2 = QA_fetch_stock_day_adv('300439', start="2018-01-06", end="2018-01-10")
        qaDAStruct3 = qaDAStruct1 + qaDAStruct2

        qaDAStruct4 = qaDAStruct3 - qaDAStruct1
        #qaDAStruct5 = qaDAStruct3 - qaDAStruct2

        list1 = []
        for iRow1 in qaDAStruct4:
            list1.append(iRow1)

        list2 = []
        for iRow2 in qaDAStruct2:
            list2.append(iRow2)

        len1 = len(list1)
        len2 = len(list2)
        for iIndex in range(len1):
            aRow = list1[iIndex]
            bRow = list2[iIndex]
            #  ????????????????????????
            v = aRow.equals(bRow)
            self.assertEqual(v, True)

    # ????todo  ??????  __getitem__
    def test_GetItem(self):
        print("ok get item")
        qaDAStruct0 = QA_fetch_stock_day_adv('300439', start="2018-01-01", end="2018-01-10")
        #for iRow int qaDAStruct0.index:
        closePrices = qaDAStruct0.__getitem__('close')
        print(closePrices)


    def test_00(self):
      res =   QA.QA_fetch_index_day('000300', '2017-01-01', '2018-01-05')
      print(res)



    # ????todo  ??????  __getattr__
    # ????todo  ??????  ix
    # ????todo  ??????  iloc
    # ????todo  ??????  loc
    # ????todo  ??????  iloc#
    # ????todo  ??????  iloc#
    # ????todo  ??????  iloc

if __name__ == '__main__':
    unittest.main()