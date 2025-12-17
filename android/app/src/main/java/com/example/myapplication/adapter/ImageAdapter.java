package com.example.myapplication.adapter;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.example.myapplication.ImageDetailActivity;
import com.example.myapplication.R;
import com.example.myapplication.model.ChangeImage;

import java.util.List;

public class ImageAdapter extends RecyclerView.Adapter<ImageAdapter.ViewHolder> {

    Context context;
    List<ChangeImage> list;

    public ImageAdapter(Context context, List<ChangeImage> list) {
        this.context = context;
        this.list = list;
    }

    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(context)
                .inflate(R.layout.item_image, parent, false);
        return new ViewHolder(v);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        ChangeImage item = list.get(position);

        Glide.with(context)
                .load("https://your_pythonanywhere.com" + item.getImage())
                .into(holder.img);

        holder.itemView.setOnClickListener(v -> {
            Intent intent = new Intent(context, ImageDetailActivity.class);
            intent.putExtra("image_url", "https://your_pythonanywhere.com" + item.getImage());
            context.startActivity(intent);
        });
    }

    @Override
    public int getItemCount() { return list.size(); }

    class ViewHolder extends RecyclerView.ViewHolder {
        ImageView img;
        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            img = itemView.findViewById(R.id.itemImageView);
        }
    }
}
