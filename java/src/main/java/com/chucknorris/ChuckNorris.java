package com.chucknorris;

public class ChuckNorris {
    public static void main(String[] args) {
        ChuckNorrisLib lib = new ChuckNorrisLib();
        String fact = lib.getFact();
        System.out.println(fact);
        lib.close();
    }
}
