use criterion::{criterion_group, criterion_main, Criterion};
use nth_prime as np;

fn criterion_benchmark(c: &mut Criterion) {
    c.bench_function("prime 10", |b| b.iter(|| np::nth(10)));
    c.bench_function("prime 100", |b| b.iter(|| np::nth(100)));
    c.bench_function("prime 1 000", |b| b.iter(|| np::nth(1_000)));
}

criterion_group!(benches, criterion_benchmark);
criterion_main!(benches);