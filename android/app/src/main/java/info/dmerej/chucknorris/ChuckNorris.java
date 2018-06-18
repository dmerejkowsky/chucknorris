package info.dmerej.chucknorris;

import com.sun.jna.Library;
import com.sun.jna.Native;
import com.sun.jna.Pointer;

public class ChuckNorris {
    private Pointer ckPointer;

    private static CLibrary loadChuckNorrisLibrary() {
        return (CLibrary) Native.loadLibrary("chucknorris", CLibrary.class);
    }

    public interface CLibrary extends Library {
        CLibrary INSTANCE = loadChuckNorrisLibrary();

        Pointer chuck_norris_init();
        String chuck_norris_get_fact(Pointer pointer);
        void chuck_norris_deinit(Pointer pointer);
    }

    public ChuckNorris() {
        ckPointer = CLibrary.INSTANCE.chuck_norris_init();
    }

    public String getFact() {
        return CLibrary.INSTANCE.chuck_norris_get_fact(ckPointer);
    }

    public void close() {
        CLibrary.INSTANCE.chuck_norris_deinit(ckPointer);
    }
}

