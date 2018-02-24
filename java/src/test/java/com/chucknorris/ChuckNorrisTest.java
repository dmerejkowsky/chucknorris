package com.chucknorris;

import org.junit.Test;

import static org.hamcrest.CoreMatchers.containsString;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThat;

public class ChuckNorrisTest {
    @Test
    public void testGetVersion() {
        String version = ChuckNorrisLib.getVersion();
        assertEquals(version, "0.1");
    }

    @Test
    public void testGetFact() {
        ChuckNorrisLib lib = new ChuckNorrisLib();
        String fact = lib.getFact();
        assertThat(fact, containsString("Chuck Norris"));
    }

}
