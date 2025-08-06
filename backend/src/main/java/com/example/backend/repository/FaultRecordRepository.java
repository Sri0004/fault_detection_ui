package com.example.backend.repository;

import com.example.backend.model.FaultRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface FaultRecordRepository extends JpaRepository<FaultRecord, Long> {
}
