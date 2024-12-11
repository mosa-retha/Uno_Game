package Mosa.Server;


import Mosa.Domain.Dealer;
import Mosa.Domain.Player;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Gameplay implements Runnable {

    private BufferedReader receive;
    private PrintWriter send;

    public Gameplay(Socket socket, Player player, Dealer dealer) throws IOException {
       socket = socket;
       receive = new BufferedReader(new InputStreamReader( socket.getInputStream()));
       send = new PrintWriter(socket.getOutputStream(), true);
    }

    @Override
    public void run() {

    }
}
