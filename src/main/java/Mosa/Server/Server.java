package Mosa.Server;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {


    public static void main(String[] args) throws Exception {
        ServerSocket serverSocket = new ServerSocket(8080);
        System.out.println("Server is running on port 8080");
        System.out.println("Waiting for client to connect...");
        Socket client = serverSocket.accept();
        System.out.println("Client connected");


        PrintWriter sender = new PrintWriter(client.getOutputStream(), true);
        BufferedReader receiver = new BufferedReader(new InputStreamReader(client.getInputStream()));


    }
}
