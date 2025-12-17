package com.example.myapplication;


import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import android.os.Bundle;
import android.widget.Toast;

import com.example.myapplication.adapter.ImageAdapter;
import com.example.myapplication.api.ApiService;
import com.example.myapplication.api.RetrofitInstance;
import com.example.myapplication.model.ChangeImage;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        loadImages();
    }

    private void loadImages() {
        ApiService api = RetrofitInstance.getApi();
        api.getImageList().enqueue(new Callback<List<ChangeImage>>() {
            @Override
            public void onResponse(Call<List<ChangeImage>> call, Response<List<ChangeImage>> res) {
                if (res.isSuccessful()) {
                    recyclerView.setAdapter(new ImageAdapter(MainActivity.this, res.body()));
                } else {
                    Toast.makeText(MainActivity.this, "Load failed", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<List<ChangeImage>> call, Throwable t) {
                Toast.makeText(MainActivity.this, "Network Error", Toast.LENGTH_SHORT).show();
            }
        });
    }
}