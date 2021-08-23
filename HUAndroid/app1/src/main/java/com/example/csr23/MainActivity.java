package com.example.csr23;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        EditText editText = findViewById(R.id.ed_name);
        EditText secondname = findViewById(R.id.ed_secondname);
        Button button = findViewById(R.id.btn_ok);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name = editText.getText().toString();
                String sname = secondname.getText().toString();
                Intent intent = new Intent(MainActivity.this, GameActivity.class);
                intent.putExtra("name",name);
                intent.putExtra("second_name",sname);
                startActivity(intent);
            }
        });
    }
}