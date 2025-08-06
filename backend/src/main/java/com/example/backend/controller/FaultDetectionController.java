package com.example.backend.controller;

import com.example.backend.model.FaultRecord;
import com.example.backend.service.FaultDetectionService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/faults")
@CrossOrigin(origins = "*")
public class FaultDetectionController {

    private final FaultDetectionService service;

    public FaultDetectionController(FaultDetectionService service) {
        this.service = service;
    }

    @GetMapping
    public List<FaultRecord> getAll() {
        return service.getAllRecords();
    }

    @PostMapping
    public FaultRecord add(@RequestBody FaultRecord record) {
        return service.addRecord(record);
    }
}
