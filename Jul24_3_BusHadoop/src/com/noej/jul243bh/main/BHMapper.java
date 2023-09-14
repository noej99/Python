package com.noej.jul243bh.main;

import java.io.IOException;
import java.text.SimpleDateFormat;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class BHMapper extends Mapper<Object, Text, Text, LongWritable> {
	private static final SimpleDateFormat SDF = new SimpleDateFormat("yyyyMMdd");
	private static final SimpleDateFormat SDF2 = new SimpleDateFormat("E");
	
	private static final Text YOIL = new Text();
	private static final LongWritable SUM = new LongWritable();
	private static final LongWritable ONE = new LongWritable();
	
	@Override
	protected void map(Object key, Text value, Mapper<Object, Text, Text, LongWritable>.Context context)
			throws IOException, InterruptedException {
		try {
			String[] line = value.toString().split(",");
			String yoil = SDF2.format(SDF.parse(line[0] + line[1] + line[2]));
			
			YOIL.set(yoil + "_합");
			SUM.set(Long.parseLong(line[line.length - 1]) + Long.parseLong(line[line.length - 2]));
			context.write(YOIL, SUM); // 월_합, 6000
			
			YOIL.set(yoil + "_데이터수");
			context.write(YOIL, ONE);
		} catch (Exception e) {
		}
		
	}
}
