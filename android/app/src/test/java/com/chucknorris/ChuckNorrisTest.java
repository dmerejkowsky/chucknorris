package com.chucknorris;

import org.junit.Test;

import static org.junit.Assert.*;

public class ChuckNorrisTest {
    @Test
    public void testGetVersion() {
        String version = ChuckNorrisLib.getVersion();
        assertEquals(version, "0.1");
    }
}
