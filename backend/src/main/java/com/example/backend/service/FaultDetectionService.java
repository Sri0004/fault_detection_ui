package com.example.backend.service;

import com.example.backend.model.FaultRecord;
import com.example.backend.repository.FaultRecordRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class FaultDetectionService {

    private final FaultRecordRepository repository;

    public FaultDetectionService(FaultRecordRepository repository) {
        this.repository = repository;
    }

    public List<FaultRecord> getAllRecords() {
        return repository.findAll();
    }

    public FaultRecord addRecord(FaultRecord record) {
        return repository.save(record);
    }
}
