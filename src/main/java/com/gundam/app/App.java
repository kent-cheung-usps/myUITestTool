package com.gundam.app;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * Hello world!
 */
public class App {
	public static void main(String[] args) {

		try {
			// Construct the command to execute the Python script
			String[] command = { "python", "pyTools/extractPasscode.py" };

			// Run the command
			Process process = Runtime.getRuntime().exec(command);

			// Capture the output of the Python script
			BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
			String line;
			while ((line = reader.readLine()) != null) {
				System.out.println(line);
			}

			// Wait for the process to complete
			int exitCode = process.waitFor();
			if (exitCode != 0) {
				System.err.println("Error: Python script execution failed.");
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}