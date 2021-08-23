package com.example.csr23;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

public class GameActivity extends AppCompatActivity {

    int inx = 0;
    static public final int WIN_LEVEL = 25;
    static public final int FAKE_LEVEL = 18;
    TextView tv_scores;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game);
        TextView textName = findViewById(R.id.tv_name);
        Intent intent = getIntent();
        String name = intent.getStringExtra("name");
        String secondname = intent.getStringExtra("second_name");
        Log.d("tag", "First name: " + name );
        Log.d("tag", "Second name: " + secondname);
        textName.setText(name + ' ' + secondname);

        tv_scores = findViewById(R.id.tv_score);
    }

    public void onClick(View view) {
        inx++;
        if(inx < FAKE_LEVEL) {
            tv_scores.setText("scores: " + inx);
        } else if (inx > WIN_LEVEL) {
            Intent intent = new Intent(this, WinActivity.class);
            intent.putExtra("scores", inx);
            intent.putExtra("name", getIntent().getStringExtra("name"));
            startActivity(intent);
        }
    }
}