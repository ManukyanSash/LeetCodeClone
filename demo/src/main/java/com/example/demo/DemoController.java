package com.example.demo;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.Map;

@RestController
public class DemoController {
    @RequestMapping("/")
    @CrossOrigin(origins = "*")
    public String demo(){
        return "Hello";
    }

    
    @PostMapping("/example")
    @CrossOrigin(origins = "*")
    public ResponseEntity<ResponseData> exampleEndpoint(@RequestBody Map<String, Object> request) {
        String solution = (String) request.get("solution");
        String language = (String) request.get("lang");
        try {
            String filename = "runtime_test/Solution." + language;
            FileWriter writer = new FileWriter(filename);
            writer.write(solution);
            writer.close();

            ProcessBuilder processBuilder = new ProcessBuilder("python3", "compile_test/main.py", filename);
            processBuilder.redirectErrorStream(true);
        
            Process process = processBuilder.start();
            //int exitCode = process.waitFor();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }
            process.waitFor();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        } catch (InterruptedException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        ObjectMapper objectMapper = new ObjectMapper();
        ResponseData responseData = null;
        try {
            responseData = objectMapper.readValue(new File("res.json"), ResponseData.class);
            return ResponseEntity.ok(responseData);
        } catch (IOException e) {
            e.printStackTrace();
        }
        return ResponseEntity.badRequest().build();
        
    }

}
