import pytest
from src.roman_converter import convert

def test_converts_1_to_I():
    assert convert(1) == "I"

def test_converts_2_to_II():
    assert convert(2) == "II"    

def test_converts_3_to_III():       
    assert convert(3) == "III"        

def test_converts_4_to_IV():       
    assert convert(4) == "IV" 

def test_converts_5_to_V():       
    assert convert(5) == "V" 
                     
def test_converts_6_to_VI():       
    assert convert(6) == "VI" 

def test_converts_7_to_VII():       
    assert convert(7) == "VII" 

def test_converts_8_to_VIII():       
    assert convert(8) == "VIII" 
                                                                                              
def test_converts_10_to_X():       
    assert convert(10) == "X" 

def test_converts_9_to_IX():       
    assert convert(9) == "IX" 
                                                                                                             
def test_converts_14_to_XIV():       
    assert convert(14) == "XIV" 

def test_converts_24_to_XXIV():       
    assert convert(24) == "XXIV" 

def test_converts_50_to_L():       
    assert convert(50) == "L" 
   
def test_converts_100_to_C():       
    assert convert(100) == "C" 
   











