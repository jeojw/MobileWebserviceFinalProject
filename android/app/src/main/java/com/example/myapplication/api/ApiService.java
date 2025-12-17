package com.example.myapplication.api;

import com.example.myapplication.model.ChangeImage;

import java.util.List;
import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Url;

public interface ApiService {
    @GET("list/")
    Call<List<ChangeImage>> getImageList();

    @GET
    Call<okhttp3.ResponseBody> loadImage(@Url String url);
}

