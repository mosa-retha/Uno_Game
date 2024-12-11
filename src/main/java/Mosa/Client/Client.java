package Mosa.Client;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Client {


    public static void main(String[] args) throws Exception {
        try {

            BufferedReader userInputReader = new BufferedReader(new InputStreamReader(System.in));
            Socket socket = new Socket("localhost", 8080);





            PrintWriter sender = new PrintWriter(socket.getOutputStream(), true);
            ClientHelper clientHelper = new ClientHelper(socket);
            Thread thread = new Thread(clientHelper);
            thread.start();


            boolean running = true;

                while (running) {

                    String userInput = userInputReader.readLine().trim();

                    if (userInput.equalsIgnoreCase("quit") || !thread.isAlive()) {
                        System.out.println("Goodbye");
                        running = false;
                    }

                    sender.println(userInput);
                }
        } catch (IOException e) {
            System.out.println("Server is not running");
        }

    }
}
